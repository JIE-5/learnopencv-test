import cv2 as cv
from PIL import Image
import numpy as np



def contours_demo(image):
    image = np.array(image, np.uint16)
    image = image.crop((10, 290, 10, 210))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary_image', binary)

    contours, heriachy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (10, 10, 255), 2)
        print(i)
    cv.imshow('detect_contours', image)


print('-----Hello Python------')
src = cv.imread('/home/jie-5/桌面/image/reba/timg.jpeg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
contours_demo(src)

cv.waitKey(0)
cv.destroyWindow()