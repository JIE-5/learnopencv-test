import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def hist2D_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv.imshow('hist_2D', hist)
    plt.imshow(hist)
    plt.title('2D—Histogram')
    plt.show()


def break_projection_demo(sample, target):
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show images
    cv.imshow('sample', sample)
    cv.imshow('target', target)

    roiHis = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roiHis, roiHis, 0, 255, cv.NORM_MINMAX)  # 规划到 [0，255]
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHis, [0, 180, 0, 256], 1)
    cv.imshow('calcBackProject', dst)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1_test.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
hist2D_demo(src)
break_projection_demo(src, src1)
cv.waitKey(0)
cv.destroyWindow()
