import logging
import contextlib
import os
import socket
import subprocess
import threading
import time

import cv2 as cv
import numpy as np
import imutils

from base import Singleton

from collections import deque
import matplotlib.pyplot as plt
from sklearn import linear_model

lsj = "lsj"

logger = logging.getLogger(__name__)

DEFAULT_DISTANCE = 0.30
DEFAULT_SPEED = 10
DEFAULT_DEGREE = 10

FRAME_X = int(960)
FRAME_Y = int(720)
FRAME_AREA = FRAME_X * FRAME_Y

FRAME_SIZE = FRAME_AREA * 3
FRAME_CENTER_X = FRAME_X / 2
FRAME_CENTER_Y = FRAME_Y / 2

CMD_FFMPEG = (f'ffmpeg -hwaccel auto -hwaccel_device opencl -i pipe:0 '
              f'-pix_fmt bgr24 -s {FRAME_X}x{FRAME_Y} -f rawvideo pipe:1')

#FACE_DETECT_XML_FILE = './droneapp/models/haarcascade_frontalface_default.xml'

#SNAPSHOT_IMAGE_FOLDER = './droneapp/static/img/snapshots/'


#Ball tracking
COLOR_LOWER = (20,89,119)    #색상값 범위
COLOR_UPPER = (84,236,254)
MAX_Q_SIZE = 64   #큐 크기`
MAX_XY_SIZE = 30  #x,y를 저장할 큐의 크기
CANNOT_CATCH = 0
bef_ball_x = int(FRAME_X/2) #이전 공 X좌표 위치
bef_ball_y = int(FRAME_Y/2)
start_time = time.time()
Q = deque(maxlen=MAX_Q_SIZE)  #디큐의 최대 버퍼 크기 설정
X = deque(maxlen = MAX_XY_SIZE)      #속도를 계산하기 위해 X좌표만 저장하는 큐를 따로 둔다.
Y = deque(maxlen = MAX_XY_SIZE)
time_X = deque(maxlen = MAX_XY_SIZE)
#log_file = 


class ErrorNoFaceDetectXMLFile(Exception):
    """Error no face detect xml file"""


class ErrorNoImageDir(Exception):
    """Error no image dir"""


class DroneManager(metaclass=Singleton):
    def __init__(self, host_ip='192.168.10.2', host_port=8889,
                 drone_ip='192.168.10.1', drone_port=8889,
                 is_imperial=False, speed=DEFAULT_SPEED):
        self.host_ip = host_ip
        self.host_port = host_port
        self.drone_ip = drone_ip
        self.drone_port = drone_port
        self.drone_address = (drone_ip, drone_port)
        self.is_imperial = is_imperial
        self.speed = speed
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host_ip, self.host_port))

        self.response = None
        self.stop_event = threading.Event()
        self._response_thread = threading.Thread(target=self.receive_response,
                                           args=(self.stop_event, ))
        self._response_thread.start()
        
        self.proc = subprocess.Popen(CMD_FFMPEG.split(' '),
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE)
        self.proc_stdin = self.proc.stdin
        self.proc_stdout = self.proc.stdout

        self.video_port = 11111

        self.user_mode = 0
        self._receive_video_thread = threading.Thread(
            target=self.receive_video,
            args=(self.stop_event, self.proc_stdin,
                  self.host_ip, self.video_port,))
        self._receive_video_thread.start()


        self.video_frame = None

        # if not os.path.exists(FACE_DETECT_XML_FILE):
        #     raise ErrorNoFaceDetectXMLFile(f'No {FACE_DETECT_XML_FILE}')
        # self.face_cascade = cv.CascadeClassifier(FACE_DETECT_XML_FILE)
        # self._is_enable_face_detect = False

        # if not os.path.exists(SNAPSHOT_IMAGE_FOLDER):
        #     raise ErrorNoImageDir(f'{SNAPSHOT_IMAGE_FOLDER} does not exists')
        self.is_snapshot = False

        self._command_semaphore = threading.Semaphore(1)
        self._command_thread = None

        self.send_command('command')
        self.send_command('streamon')
        self.set_speed(self.speed)
        self.zero = 0

    def receive_response(self, stop_event):
        while not stop_event.is_set():
            try:
                self.response, ip = self.socket.recvfrom(3000)
                logger.info({'action': 'receive_response',
                             'response': self.response})
            except socket.error as ex:
                logger.error({'action': 'receive_response',
                             'ex': ex})
                break

    
    def __dell__(self):
        self.stop()

    def stop(self):
        self.stop_event.set()
        retry = 0
        while self._response_thread.isAlive():
            time.sleep(0.3)
            if retry > 30:
                break
            retry += 1
        self.socket.close()
        os.kill(self.proc.pid, 9)
        # Windows
        # import signal
        # os.kill(self.proc.pid, signal.CTRL_C_EVENT)

    def send_command(self, command, blocking=True):
        self._command_thread = threading.Thread(
            target=self._send_command,
            args=(command, blocking,))
        self._command_thread.start()

    def _send_command(self, command, blocking=True):
        is_acquire = self._command_semaphore.acquire(blocking=blocking)
        if is_acquire:
            with contextlib.ExitStack() as stack:
                stack.callback(self._command_semaphore.release)
                logger.info({'action': 'send_command', 'command': command})
                self.socket.sendto(command.encode('utf-8'), self.drone_address)

                retry = 0
                while self.response is None:
                    time.sleep(0.3)
                    if retry > 3:
                        break
                    retry += 1

                if self.response is None:
                    response = None
                else:
                    response = self.response.decode('utf-8')
                self.response = None
                return response

        else:
            logger.warning({'action': 'send_command', 'command': command, 'status': 'not_acquire'})

    def takeoff(self):
        return self.send_command('takeoff')

    def land(self):
        return self.send_command('land')

    def move(self, direction, distance):
        distance = float(distance)
        if self.is_imperial:
            distance = int(round(distance * 30.48))
        else:
            distance = int(round(distance * 100))
        return self.send_command(f'{direction} {distance}')

    def up(self, distance=DEFAULT_DISTANCE):
        return self.move('up', distance)

    def down(self, distance=DEFAULT_DISTANCE):
        return self.move('down', distance)

    def left(self, distance=DEFAULT_DISTANCE):
        return self.move('left', distance)

    def right(self, distance=DEFAULT_DISTANCE):
        return self.move('right', distance)

    def forward(self, distance=DEFAULT_DISTANCE):
        return self.move('forward', distance)

    def back(self, distance=DEFAULT_DISTANCE):
        return self.move('back', distance)

    def set_speed(self, speed):
        return self.send_command(f'speed {speed}')

    def clockwise(self, degree=DEFAULT_DEGREE):
        return self.send_command(f'cw {degree}')

    def counter_clockwise(self, degree=DEFAULT_DEGREE):
        return self.send_command(f'ccw {degree}')
    
    def receive_video(self, stop_event, pipe_in, host_ip, video_port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock_video:
            sock_video.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock_video.settimeout(.5)
            sock_video.bind((host_ip, video_port))
            data = bytearray(2048)
            while not stop_event.is_set():
                try:
                    size, addr = sock_video.recvfrom_into(data)
                    # logger.info({'action': 'receive_video', 'data': data})
                except socket.timeout as ex:
                    logger.warning({'action': 'receive_video', 'ex': ex })
                    time.sleep(0.5)
                    continue
                except socket.error as ex:
                    logger.error({'action': 'receive_video', 'ex': ex})
                    break

                try:
                    pipe_in.write(data[:size])
                    pipe_in.flush()
                except Exception as ex:
                    logger.error({'action': 'receive_video', 'ex': ex})
                    break


    def video_binary_generator(self):
        while True:
            try:
                frame = self.proc_stdout.read(FRAME_SIZE)
            except Exception as ex:
                logger.error({'action': 'video_binary_generator', 'ex': ex})
                continue

            if not frame:
                continue

            frame = np.fromstring(frame, np.uint8).reshape(FRAME_Y, FRAME_X, 3)
            #print(frame)
            yield frame

    # def enable_face_detect(self):
    #     self._is_enable_face_detect = True

    # def disable_face_detect(self):
    #     self._is_enable_face_detect = False

    def video_jpeg_generator(self):
        global bef_ball_x , bef_ball_y, CANNOT_CATCH, start_time
        global Q,X,Y,time_X
        for frame in self.video_binary_generator():
            #cv.imshow("Frame", frame)
            yield frame

            # ###ball tracking###
            # bef_command_time = 0
            # drone_move_distance = 0
            # drone_move_time = 1
            # drone_move_speed = 100
            # if self.user_mode == 1 :
            #     cur_time = time.time()
            #     blurred = cv.GaussianBlur(frame, (11, 11), 0)  #공만 표시하기위해 이미지를 흐리게
            #     hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)  #HSV색 공간으로 바군다.

            #             #녹색공이 어딨는지 파악 후 얼룩 제거
            #     mask = cv.inRange(hsv, COLOR_LOWER, COLOR_UPPER) 
            #     mask = cv.erode(mask, None, iterations=2)      #얼룩 제거
            #     mask = cv.dilate(mask, None, iterations=2)

            #     contours = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            #     contours = imutils.grab_contours(contours)
            #     center = None

            #     x = 0   #현재 공 위치
            #     y = 0

            #     if len(contours) > 0:
            #         CANNOT_CATCH = 0
            #         max_circle = max(contours, key=cv.contourArea)
            #         (x, y), radius = cv.minEnclosingCircle(max_circle)

            #         #print(int(x), int(y))
            #         M = cv.moments(max_circle)
            #         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            #     else :
            #         x = bef_ball_x
            #         y = bef_ball_y
            #         if CANNOT_CATCH == 0 :
            #             CANNOT_CATCH = time.time()
            #         else :
            #             if time.time()-CANNOT_CATCH > 3 :
            #                 print("ball lost!!")
            #                 #mode = set_user_mode()
                
            #     Q.appendleft(center)  #큐에 좌표를 넣는다.
            #     X.append(int(x - FRAME_X/2))    #X큐와 Y큐를 합치면 Q가 되지만 속도를 위해 따로 만듦
            #     Y.append(int(y - FRAME_Y/2))   
            #     time_X.append(cur_time - start_time)    #시작하고 지난 시간을 저장
                
                
            #     cv.line(frame, (int(x),int(y)), (int(x),int(y)), (0,0,255),  5) #현재 공의 위치를 점으로 찍는다.
            #     bef_ball_x = x  
            #     bef_ball_y = y
            #     #cv.imshow("Frame", frame)
            #     key = cv.waitKey(1) & 0xFF 
                
                
                
            #     #속도 계산
            #     dx = X[len(X)-1] - X[0]
            #     drone_speed = int(abs(dx) / (FRAME_X / 100))
            #     print(drone_speed)
            #     #drone.set_speed(drone_speed)
                
                
            #     #머신 러닝을 통해 공의 위치를 예측하여 오인식율을 낮춘다.
            #     N = 6
            #     predictions_x = 0
            #     predictions_y = 0
                
            #     if cur_time - start_time > 3 :  #3초 후부터 공의 위치를 예측한다.
            #         graph_X = [[time_X[k] ** n for n in range(1, N)] for k in range(len(time_X))]            
            #         reg = linear_model.LinearRegression()   #LinearRegression 예측 모델 사용
            #         reg.fit(graph_X,X)

            #         pre_inp = [(cur_time - start_time + 0.014) ** n for n in range(1, N)]
            #         predictions_x = reg.predict([pre_inp])[0] + int(FRAME_X/2)
            #         if FRAME_X < predictions_x :
            #             predictions_x = FRAME_X
            #         if 0 > predictions_x :
            #             predictions_x = 0

                        
            #         #print(predictions_x)
            #         reg = linear_model.LinearRegression()
            #         reg.fit(graph_X,Y)
                    
            #         pre_inp = [(cur_time - start_time + 0.014) ** n for n in range(1, N)]
            #         predictions_y = reg.predict([pre_inp])[0] + int(FRAME_Y/2)
            #         if FRAME_Y < predictions_y :
            #             predictions_y = FRAME_X
            #         if 0 > predictions_y :
            #             predictions_y = 0
            #         #print(predictions_y)
                    
            #         #print(int(predictions_x - FRAME_X/2), int(predictions_y- FRAME_X/2))
            #         cv.circle(frame, (int(predictions_x), int(predictions_y)), 30, (0, 255, 255), 2)
            #         #print(f'next : {predictions_x} {predictions_y}')
            #     #print(x, y)
            #     print(x, drone_speed)


            #     if cur_time - bef_command_time > drone_move_time :
            #         # if x < FRAME_CENTER_X :
            #         #     self.send_command(f'go 0 20 0 100', blocking=False) 
            #         # else :
            #         #     self.send_command(f'go 0 -20 0 80', blocking=False) 
            #         drone_move_distance =int((FRAME_CENTER_X-x)/(FRAME_X/100))
            #         self.send_command(f'go 0 {drone_move_distance} 0 {drone_move_speed}', blocking=False) 
            #         bef_command_time = cur_time
            #         drone_move_time = drone_move_distance/drone_move_speed



                #cv.imshow("Frame", frame)            
                


                #key = cv.waitKey(1) & 0xFF 
                #if key == ord("q"):
                #    break





            # if self._is_enable_face_detect:
            #     if self.is_patrol:
            #         self.stop_patrol()

            #     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            #     faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            #     for (x, y, w, h) in faces:
            #         cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            #         face_center_x = x + (w/2)
            #         face_center_y = y + (h/2)
            #         diff_x = FRAME_CENTER_X - face_center_x
            #         diff_y = FRAME_CENTER_Y - face_center_y
            #         face_area = w * h
            #         percent_face = face_area / FRAME_AREA

            #         drone_x, drone_y, drone_z, speed = 0, 0, 0, self.speed
            #         if diff_x < -30:
            #             drone_y = -30
            #         if diff_x > 30:
            #             drone_y = 30
            #         if diff_y < -15:
            #             drone_z = -30
            #         if diff_y > 15:
            #             drone_z = 30
            #         if percent_face > 0.30:
            #             drone_x = -30
            #         if percent_face < 0.02:
            #             drone_x = 30
            #         self.send_command(f'go {drone_x} {drone_y} {drone_z} {speed}',
            #                           blocking=False)
            #         break

            _, jpeg = cv.imencode('.jpg', frame)
            jpeg_binary = jpeg.tobytes()

            # if self.is_snapshot:
            #     backup_file = time.strftime("%Y%m%d-%H%M%S") + '.jpg'
            #     snapshot_file = 'snapshot.jpg'
            #     for filename in (backup_file, snapshot_file):
            #         file_path = os.path.join(
            #             SNAPSHOT_IMAGE_FOLDER, filename)
            #         with open(file_path, 'wb') as f:
            #             f.write(jpeg_binary)
            #     self.is_snapshot = False

            #yield jpeg_binary

    def snapshot(self):
        self.is_snapshot = True
        retry = 0
        while retry < 3:
            if not self.is_snapshot:
                return True
            time.sleep(0.1)
            retry += 1
        return False
