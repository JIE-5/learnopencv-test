import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    th = 256
    tw = 256
    h, w = image.shape[:2]
    print(h)
    print(w)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, th):
        for col in range(0, w, tw):
            roi = gray[row: row+th, col: col+tw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 51, 10)
            gray[row: row+th, col: col+tw] = dst
    cv.imwrite('C:/Users/JIE/Desktop/illustration/picture/big_image_binary.jpg', gray)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
big_image_binary(src)

cv.waitKey(0)
cv.destroyWindow()