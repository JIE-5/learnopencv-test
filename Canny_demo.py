import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (7, 7), 0)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 80, 150)
    cv.imshow('edge_grad', edge_output)

    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow('Color Edge', dst)


print('-----Hello Python------')
src = cv.imread('/home/jie-5/桌面/image/reba/iamge1.jpg')
src1 = cv.imread('/home/jie-5/桌面/image/reba/image2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
edge_demo(src)

cv.waitKey(0)
cv.destroyWindow()