import cv2 as cv
import numpy as np


# 反转
def access_pixels(image):
    print(image.shape)
    hight = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('width:%s, hight:%s, channels:%s' % (width, hight, channels))
    for raw in range(hight):
        for col in range(width):
            for c in range(channels):
                pv = image[raw, col, c]
                image[raw, col, c] = 255 - pv
    cv.imshow('pixel_demo', image)


def create_image():
    """
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 255
    cv.imshow('new_img', img)
    """
    img = np.ones([800, 800, 3], np.uint8)
    print('--------------')
    img[:, :, 0] = img[:, :, 0]*255
    img[:, :, 1] = img[:, :, 1]*80
    img[:, :, 2] = img[:, :, 2]*255
    print(type(img))
    cv.imshow("new_image", img)
    cv.imwrite('C:/Users/JIE/Desktop/illustration/New_image.png', img)
    m1 = np.ones([2, 2], np.uint8)
    m1.fill(4)
    print(m1)


src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1.jpg')
cv.namedWindow('imput image', cv.WINDOW_AUTOSIZE)
cv.imshow('imput image', src)
# access_pixels(src)
create_image()
cv.waitKey(0)
cv.destroyWindow('imput image')
