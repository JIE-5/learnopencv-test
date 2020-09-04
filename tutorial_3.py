import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow('add_demo1', dst)


def subtract_demo(m1, m2):
        dst = cv.subtract(m1, m2)
        cv.imshow('add_demo2', dst)


def dividee_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('add_demo3', dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('add_demo3', dst)


def other_demo(m1, m2):                    # 打印颜色的均值和方差，分析颜色
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)
    print(dev1)
    print(dev1)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


def logic_demo(m1, m2):
    dst1 = cv.bitwise_and(m1, m2)
    dst2 = cv.bitwise_or(m1, m2)
    dst3 = cv.bitwise_not(m1, m2)
    cv.imshow('logic_demo1', dst1)
    cv.imshow('logic_demo2', dst2)
    cv.imshow('logic_demo3', dst3)


def contrast_brightness_demo(image, c, b):          # 亮度，对比度。
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow('con_bri_demo', dst)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/10.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/LinuxLogo.jpg')
src2 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/WindowsLogo.jpg')

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.namedWindow('input image1', cv.WINDOW_AUTOSIZE)
cv.namedWindow('input image2', cv.WINDOW_AUTOSIZE)

cv.imshow('input image', src)
cv.imshow('input image1', src1)
cv.imshow('input image2', src2)


'''add_demo(src1, src2)
subtract_demo(src1, src2)
dividee_demo(src1, src2)
multiply_demo(src1, src2)
other_demo(src1, src2)
logic_demo(src1, src2)'''
contrast_brightness_demo(src, 1, 16)


cv.waitKey(0)
cv.destroyWindow()
