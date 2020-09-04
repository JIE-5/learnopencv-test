import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim(0, 256)
    plt.show()


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/aima.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
# plot_demo(src)
image_hist(src)
cv.waitKey(0)
cv.destroyWindow()