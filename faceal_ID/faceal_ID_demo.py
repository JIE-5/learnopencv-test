import cv2
import numpy as np


#test
def faceal_ID_demo():
    face_casecade=cv2.CascadeClassifier('/home/jie-5/learnopencv-test/faceal_ID/haarcascade_frontalface_alt.xml')
    camera = cv2.VideoCapture(0)
    # camera.set(15, 300)
    cv2.namedWindow('face')

    while True:
        # print("exposure={}".format(camera.get(15)))

        # print(camera.get(15))
        ret, frame = camera.read()

        if not ret:
            break
        gray_farme = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_casecade.detectMultiScale(gray_farme, 1.3, 4)
        # print(face)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # print(x)
            # print(face)
        frame = cv2.flip(frame, 1)
        cv2.imshow('face', frame)
        c = cv2.waitKey(40)
        if c == 27:
            break


faceal_ID_demo()