#coding:utf8
'''
Created on 2014-6-6

@author: wangxd
'''

from cv2 import cv

def verticalProjection(img):
    "返回每一列的像素值的和的列表"
    #(w,h) = cv.GetSize(img)
    h,w = img.shape[:2]
    print 'h,w = ', h,w
    sumCols = []
    for j in range(w):
        col = cv.GetSubRect(img, (j,0,1,h))
        sumCols.append(cv.Sum(col)[0])
    return sumCols