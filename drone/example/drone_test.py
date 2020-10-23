import logging
import socket
import sys
import time

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


class DroneManager(object):
    #드론의 IP, 포트는 고정
    def __init__(self, host_ip='192.168.10.2', host_port=8889,
                 drone_ip='192.168.10.1', drone_port=8889):
        self.host_ip = host_ip
        self.host_port = host_port
        self.drone_ip = drone_ip
        self.drone_port = drone_port
        self.drone_address = (drone_ip, drone_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host_ip, self.host_port))

        #드론에 이니셜라이즈 하기 위해 commmand 와 streamon이라는 문자열을 바이너리로 보낸다.
        #command : SDK모드 시작
        #streamon : 비디오 스트림 수신
        self.socket.sendto(b'command', self.drone_address)
        self.socket.sendto(b'streamon', self.drone_address)

    def __dell__(self):
        self.stop()

    def stop(self):
        self.socket.close()

    #커맨드 전송 시 해당 커맨드를 출력
    def send_command(self, command):
        logger.info({'action': 'send_command', 'command': command})
        self.socket.sendto(command.encode('utf-8'), self.drone_address)

    def takeoff(self):
        self.send_command('takeoff')

    def land(self):
        self.send_command('land')


if __name__ == '__main__':
    drone_manager = DroneManager()
    drone_manager.takeoff()

    time.sleep(1)

    drone_manager.land()

