import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def equalHist_demo(image):                  # 直方图直接均衡化，无法改变参数
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist_demo', dst)   # 直方图均衡化，清晰图像。


def clahe_demo(image):                      # 直方图均衡化，可改变参数  ，
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=0.1, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('chahe_demo', dst)


def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            r = image[row, col, 1]
            g = image[row, col, 2]
            index = np.int(r/bsize)*16*16 + np.int(g/bsize)*16 + np.int(b/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    # plt.plot(rgbHist, color='green')
    # plt.xlim(0, 256)
    # plt.show()
    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('巴氏距离：%s， 相关性：%s， 卡方：%s'%(match1, match2, match3))


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/aima.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/2.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
equalHist_demo(src)
clahe_demo(src)
create_rgb_hist(src)
hist_compare(src, src1)


cv.waitKey(0)
cv.destroyWindow()