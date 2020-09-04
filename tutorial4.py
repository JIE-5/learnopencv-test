import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyimg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)    #注意+2
    cv.floodFill(copyimg, mask, (30, 30), (100, 10, 10), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo', copyimg)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow('fill_brinary', image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0                  # 此方式只填充为0的部分
    cv.floodFill(image, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('fill_color_demo', image)


print('-----Hello Python------')
src = cv.imread('/home/jie-5/桌面/image/reba/iamge1.jpg')
src1 = cv.imread('/home/jie-5/桌面/image/reba/iamge2.jpg')

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
print(src.shape)
some = src[400:700, 500:800]
gray = cv.cvtColor(some, cv.COLOR_BGR2GRAY)
breaksome = cv.cvtColor(gray, cv.COLOR_BGR2RGB)


fill_color_demo(src)
fill_binary()
'''cv.imshow('breaksome', breaksome)
cv.imshow('gray', gray)
cv.imshow('input image1', src)'''
print(breaksome.shape)
print(some.shape)
cv.waitKey(0)
cv.destroyWindow()





