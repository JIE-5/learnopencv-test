import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 35, 35)
    cv.imshow('bi_demo', dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 20)
    cv.imshow('shift_demo', dst)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/aima.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
bi_demo(src)
# shift_demo(src)
cv.waitKey(0)
cv.destroyWindow()