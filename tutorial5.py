import cv2 as cv
import numpy as np


def blur_demo(image):                       # 均值模糊，去噪声
    dst = cv.blur(image, (10, 10))
    cv.imshow('blur_demo', dst)


def median_blur_demo(image):                       # 中值模糊
    dst = cv.medianBlur(image, 5)
    cv.imshow('medianBlur_demo', dst)


def custom_blur_demo(image):                # 自定义模糊
    kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel= kernel)
    cv.imshow('custom', dst)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)

cv.waitKey(0)
cv.destroyWindow()
