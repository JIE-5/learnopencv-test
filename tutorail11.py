import cv2 as cv
import numpy as np


def template_demo(image1, image2):
    tpl = image1
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        target = image2.copy()
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        print(tl)
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow('match_'+np.str(md), target)
        cv.imshow('match_1' + np.str(md), result)


print('-----Hello Python------')
src = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1.jpg')
src1 = cv.imread('C:/Users/JIE/Desktop/illustration/picture/1_test.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
cv.imshow('tpl', src1)
template_demo(src1, src)

cv.waitKey(0)
cv.destroyWindow()