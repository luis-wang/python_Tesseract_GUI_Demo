#coding:utf8
'''
1.通过一段一段 水平扫描和竖直扫描，找出hist的变化,然后统计所有的hist分布，是可以确定出行的

2.由于可能图片上的文字颜色为黑色或为白色，所以得分两次检查字体 

forked from :D:\data\aptana34workspace\computer_cv\1tutroals\histograms\find_text_line_by_hori_hist.py

'''
import cv2
from math import ceil
import numpy as np
from matplotlib import pyplot as plt

min_word_width = 2  #默认最小的字宽为2，如1，i等
min_gap = 2         #最小行间距



def draw_text_lines():
    "画出文字的边缘线"
    img = cv2.imread(r'E:\2kkkkk\ocr\word_with_img\chi-eng.png')
    imgsrc = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,230,255,0)
    
    
    #cv2.imshow('thresh', thresh)
    #cv2.waitKey(0)
    
    
    print '图片高 = ',img.shape[0]
    print '图片宽= ',img.shape[1]
    
    #找出每一行中黑色的像素点的个数
    rows, cols = img.shape[:2]
    height, width = img.shape[:2]
    
    ###找出某一部分来做直方图
    
    nums = []
    flag = False
    
    for i in range(rows):
        #找出一行中有多少个零像素，0像素是黑色, thresh[i] = [255,0,0...共有一宽度个] 
        #if i ==10:print '--', thresh[i], '++',len(thresh[i])
        row_num = list(thresh[i]).count(0)  #第一行的黑点数
        nums.append(row_num )
        
        if len(nums) > 0:
            #在最近的一个0值上面画线
            b1 = row_num * nums[i-1] == 0
            b2 = row_num + nums[i-1] > 0
            
            #将边界的条件都画出来
            if b1 and b2:
                #将开始边界画绿线
                if row_num >0:
                    cv2.line(imgsrc, (0,i-1), (cols-1,i-1), (0,255,0),1)
                else:
                    cv2.line(imgsrc, (0,i), (cols-1,i), (0,0,255),1)
    
    #依次统计的是每行有多少的黑色像素       
    print nums
    
    cv2.imshow('imgsrc',imgsrc)
    cv2.waitKey()


def horizontal_hist_calcu():
    "统计出所有的水平方向直方图"
    
    #先将图片横向分割成n等分，单位是min_word_width，依次找出有多少是字体部分
    img = cv2.imread('img/small_chi.png')
    imgsrc = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,230,255,0)
    
    
    #cv2.imshow('thresh', thresh)
    #cv2.waitKey(0)
    
    
    print '图片高 = ',img.shape[0]
    print '图片宽= ',img.shape[1]
    
    #找出每一行中黑色的像素点的个数
    rows, cols = img.shape[:2]
    height, width = img.shape[:2]
    
    strip_num = ceil(width/float(min_word_width)) #找出最多有多少个条
    
    #从左到右依次把竖直的条做直方分析
    for strip_index in range(strip_num-1):
        for hight_index in range(height):
            list(thresh[strip_index : strip_index+1]).count(0)
    
    
       


if __name__ == '__main__':
    print 'start...'
    
    draw_text_lines()
    
    print 'end...'

