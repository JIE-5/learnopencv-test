import cv2 as cv
from PIL import Image
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    xgray = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygray = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgray, ygray, 200, 300)
    return edge_output


def contours_demo(image):
    image = image[10:219, 10:297]
    image = cv.GaussianBlur(image, (0, 0), 0.9)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary_image', binary)
    # binary = edge_demo(image)

    contours, heriachy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (10, 10, 255), -2)
        # print(i)
    cv.imshow('detect_contours', image)


print('-----Hello Python------')
src = cv.imread('/home/jie-5/桌面/image/reba/timg.jpeg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
contours_demo(src)

cv.waitKey(0)
cv.destroyWindow()