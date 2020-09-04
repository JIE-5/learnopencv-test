import cv2 as cv
import numpy as np


def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print(ret)
    cv.imshow('binary_img', binary)


def bi_demo(image):
    print('processing bilateralFilter')
    dst = cv.bilateralFilter(image, 0, 35, 35)
    cv.imshow('bi_demo', dst)
    return dst


def local_threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9        , 5)
    cv.imshow('local_threshold_img', dst)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/aima.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
# src = np.uint8(src)
dst = bi_demo(src)
print('processing local tgresgold demo')
local_threshold_demo(dst)

cv.waitKey(0)
cv.destroyWindow()