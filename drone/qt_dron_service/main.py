from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
#from PyQt5 import QtSql
#from PyQt5 import QtCore

# from PyQt5.QtMultimedia import *
# from PyQt5.QtMultimedia import QSound
# from PyQt5.QtMultimediaWidgets import *
# from PyQt5.QtTest import *
from PyQt5.QtGui import *

from drone_manager import DroneManager
import numpy as np

import time
import cv2
import sys
import os
import subprocess

def get_drone():
    return DroneManager()


class cameraThread(QThread):
    #mySignal = pyqtSignal(QPixmap)
    def __init__(self):
        super().__init__()
        self.drone = get_drone()

    def run(self):
        for frame in self.drone.video_binary_generator():
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imshow("frame", frame)
            key = cv2.waitKey(1) & 0xFF 
            if key == ord("q"):
               break

            #h, w, _ = frame.shape
            #img = QImage(w, h, QImage.Format_RGB32)
            # for y in range(h):
            #     for x in range(w):
            #         img.setPixel(x, y, QColor(*frame[y][x]).rgb())
            # img = QPixmap.fromImage(img)
            #print(img)
            #self.mySignal.emit(img)


class UserControlPage(QWidget):
    def __init__(self):
        super().__init__()
        #loadUi("user_control.ui", self)
        self.main()

    def main(self):
        pass

class BallTrackingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.drone = get_drone()
        self.main()

    def main(self):

        self.setFixedSize(1280,720)
        layout = QHBoxLayout()
        #layout.SetFixedSize(1280, 720)
        #self.setGeometry(0,0,1280,720)
        #layout = QFrame()
        #layout.setGeometry(960, 0, 320, 720)
        #layout.setStyleSheet("background-color:blue;")
        self.camera = QLabel("asdfaasdf" , self)
        self.camera.setMinimumWidth(960)
        #camera.setGeometry(0,0,960, 720)
        self.camera.setStyleSheet("background-color:white;")
        btns = QVBoxLayout()
        btn_take_off = QPushButton("이륙")
        btn_up = QPushButton("btn2")
        btn_down = QPushButton("btn3")
        btn_land = QPushButton("착륙")
        btn_take_off.setMinimumHeight(150)
        btn_up.setMinimumHeight(150)
        btn_down.setMinimumHeight(150)
        btn_land.setMinimumHeight(150)
        btns.addWidget(btn_take_off)
        btns.addWidget(btn_up)
        btns.addWidget(btn_down)
        btns.addWidget(btn_land)
        layout.addWidget(self.camera)
        layout.addLayout(btns)
        #layout.addWidget(btns)
        self.setLayout(layout)
        #layout.addWidget(camera)
        

        # newlayout = QVBoxLayout(self)
        # newlayout.setGeometry(QRect(0,0,100,100))

        

        btn_take_off.clicked.connect(self.takeOff)
        btn_land.clicked.connect(self.land)

        self.show()
        self.th = cameraThread()
        #self.th.mySignal.connect(self.setImage)
        self.th.start()
       
        # for frame in self.video_generator() :
        #     # cv2.imshow("frame", frame)
        #     # key = cv2.waitKey(1) & 0xFF 
        #     # if key == ord("q"):
        #     #     break
            

        #     #pass
        #     #self.data = np.array(self.data).reshape(2048,2048).astype(np.int32)
        #     img = QImage(frame, frame.shape[0], frame.shape[1], QImage.Format_RGB32)
            #print(type(img))
            #camera.setPixmap(QPixmap(img).scaledToWidth(960))
            
    def setImage(self, img):
        self.camera.setPixmap(img)
        #print(1)
        
            

    

    def takeOff(self) :
        self.drone.takeoff()
    
    def land(self) :
        self.drone.land()
        
        
        #self.setLayout(layout)
    

class FaceTrackingPage(QWidget):
    def __init__(self):
        super().__init__()
        #loadUi("face_tracking.ui", self)
        self.main()

    def main(self):
        pass

class HelpPage(QWidget):
    def __init__(self):
        super().__init__()
        #loadUi("help.ui", self)
        self.main()

    def main(self):
        pass


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.main()

    def main(self):
        img = QImage("img/drone2.jpg")
        self.label_img.setPixmap(QPixmap(img).scaledToWidth(720))
        self.label_user.mousePressEvent = self.go_control
        self.label_ball.mousePressEvent = self.go_ball
        self.label_face.mousePressEvent = self.go_face
        self.label_help .mousePressEvent = self.go_help

    def go_control(self, mode = 1):
        pass

    def go_ball(self, mode = 2):
        self.new_win = BallTrackingPage()

    def go_face(self, mode = 3):
        pass

    def go_help(self, mode = 4):
        pass


def main():
    app = QApplication([])
    win = MainWindow()
    #win.showFullScreen()
    win.show()
    app.exec()


if __name__ == "__main__":
    # execute only if run as a script
    main()