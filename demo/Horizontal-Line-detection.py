#coding:utf-8
#基于python2.7
import numpy as np
import cv2,math

img = cv2.imread("img/textfile.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 120)
lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
for line in lines[0]:
    pt1 = (line[0],line[1])
    pt2 = (line[2],line[3])
    cv2.line(img, pt1, pt2, (0,0,255), 3)
#cv2.imwrite("C:/temp/2.png", img)


cv2.imshow('winname', img)
cv2.waitKey(0)
cv2.destroyAllWindows()