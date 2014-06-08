#coding:utf8
'''
Created on 2014-6-6

@author: wangxd
'''

from cv2 import cv
import cv2


def verticalProjection(img):
    "返回每一列的像素值的和的列表"
    imgsrc = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,230,255,0)
    
    cv2.imshow('thresh' ,thresh)

    
    rows, cols = img.shape[:2]
    height, width = img.shape[:2]
    
    print '图片高 = ',height
    print '图片宽= ',width    

    nums = []
    flag = False    
    
    for c in range(cols):
        #找出一列中有多少个零像素，0像素是黑色, thresh[i] = [255,0,0...共有一宽度个] 
        #if i ==10:print '--', thresh[i], '++',len(thresh[i])
        
        #找出一列的所有像素值
        col_pix = [thresh[r][c] for r in range(rows)]
        col_num = col_pix.count(0)  #每一列的黑点数
        nums.append( col_num )
        
        #将字与字之间的空间部分画出线条
        if col_num < 2:
            #将开始边界画绿线
            cv2.line(imgsrc, (c,0), (c,height), (0,0,255),1)
    
    #依次统计的是每行有多少的黑色像素       
    print nums
    
    cv2.imshow('imgsrc-rect',imgsrc)
    cv2.waitKey(0)    
    
    


if __name__ == '__main__':
    '''
    l1 = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]
    
    print l1[0][0],l1[1][0],l1[2][0]
    rows = 4
    print [l1[r][0] for r in range(rows)]
    '''
    pass



