import cv2
import numpy as np


def faceal_ID_demo():
    face_casecade=cv2.CascadeClassifier('/home/jie-5/learnopencv-test/faceal_ID/haarcascade_frontalface_alt.xml')
    camera = cv2.VideoCapture(0)
    cv2.namedWindow('face')

    while True:
        ret, farme = camera.read()
        if ret :
            gray_farme = cv2.cvtColor(farme, cv2.COLOR_BGR2GRAY)
            face = face_casecade.detectMultiScale(gray_farme, 1.3, 2)
            cv2.imshow('face', farme)


faceal_ID_demo()