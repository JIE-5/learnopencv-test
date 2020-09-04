import cv2 as cv
import numpy as np


def extrace_object():  # 颜色识别
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if not ret:                 # ret == False 一样的
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([35, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mark = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow('video', frame)
        cv.imshow('video', mark)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    cv.imshow('YUV', yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('Ycrcb', Ycrcb)


src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1.jpg')
cv.namedWindow('imput image', cv.WINDOW_AUTOSIZE)
cv.imshow('imput image', src)
extrace_object()
b, g, r = cv.split(src)  # 通道分离
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

src = cv.merge([b, g, r])  # 通道合并
# src[:, :, 2] = 0
# src[:, :, 0] = 100


# cv.imshow('111', src)

cv.waitKey(0)
cv.destroyWindow('imput image')
