'''
Created on 2014-2-18

@author: Administrator
'''
import cv2
import numpy as np

img = cv2.imread('img/alllines.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,150,200,apertureSize = 3)

cv2.imshow('edges',edges)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength = 5, maxLineGap = 10)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('houghlines',img)

cv2.waitKey(0)
cv2.destroyAllWindows()