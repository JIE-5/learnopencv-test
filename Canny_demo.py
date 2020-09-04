import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv. GaussianBlur(image, (3, 3), 0)



print('-----Hello Python------')
src = cv.imread('/home/jie-5/桌面/image/reba/iamge1.jpg')
src1 = cv.imread('/home/jie-5/桌面/image/reba/image2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)


cv.waitKey(0)
cv.destroyWindow()