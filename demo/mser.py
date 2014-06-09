#!/usr/bin/env python

'''
MSER detector demo
==================
mser.py [<video source>]

ESC   - exit
Maximally stable extremal region extractor


forked from python2/mser.py
'''
import os,sys
sys.path.append(r'D:\workspaces\aptana3\openvc_demo\python2')
sys.path.append(r'D:\data\aptana34workspace\computer_cv\python2')


import numpy as np
import cv2
import video

def official_method():
    try: video_src = sys.argv[1]
    except: video_src = 0

    cam = video.create_capture(video_src)
    mser = cv2.MSER()
    while True:
        #ret, img = cam.read()
        img = cv2.imread('img/eng_text.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()

        regions = mser.detect(gray, None)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
        cv2.polylines(vis, hulls, 1, (0, 255, 0))

        cv2.imshow('img', vis)
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()    



if __name__ == '__main__':

    mser = cv2.MSER()

    #ret, img = cam.read()
    #img = cv2.imread('img/eng_text.png')
    img = cv2.imread(r'F:\Recovery\bigchi.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    
    vis = img.copy()

    regions = mser.detect(gray, None)
    print 'type regions : ',type(regions[0])
    
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))

    cv2.imshow('img', vis)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
