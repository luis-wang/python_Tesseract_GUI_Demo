#coding=utf-8
"""
下一步，怎么把汉字从一行中分割出来 

"""
import cv2
import numpy as np
from utils import verticalProjection


min_line_hight  = 10        #最小的字体高度
min_line_space  = 3         #最小的行间距
dilate_kernel   = (2,2)     #放大时的把字体变得粗一点的核心 ,这个应该根据不同的字体变化,这个值不能大于行间距

rect_left_margin= 4         #矩形框左边需要左移多少
rect_top_margin = 3         #上边上移多少


def imshow(title,img,flag=False):
    "控制是不是显示出所有的窗口"
    if flag:
        cv2.imshow(title, img)


#第一步进行二值化，不作任何放大腐蚀等操作
def binarize(img, args=None):
    "采用适应高斯二值化"
    thr = cv2.adaptiveThreshold(img,
                                255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,
                                
                                
                                11,2)
    
    return thr
    

#一般情况都是白纸黑字，也有少数情况小区域是相反的
def find_text_foreground(img):
    img = cv2.bitwise_not(img)
    return img


def cv2_dilate(img):
    kernel = np.ones(dilate_kernel, np.uint8)
    print 'kernel = ', kernel
    return cv2.dilate(img,kernel,iterations = 1)  


def get_text_area(img, w1,h1, kernel):
    "把字体一行一行地变成长矩形条"

    #可以把字体中的小黑点去掉
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)    


def find_text_rects(img):
    "找出矩形"
    contours, hierarchy = cv2.findContours(img,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_res_img():
    "可供别的代码调用的接口"
    f = [
         'testimg/text/chi-eng.tiff',
         'testimg/text/eng-chi.png',
         'testimg/text/chi0.png',]
    
    imsrc = cv2.imread(f[0])
    img = cv2.cvtColor(imsrc, cv2.COLOR_BGR2GRAY)
    
    #原图像
    imshow("Origin", imsrc)
    
    mw, mh = img.shape[1],img.shape[0]
    #print "长=%s 宽=%s" % (mw, mh)
    
    #1.二值化
    img = binarize(img)
    
    #2.取反图像,找出白色的字体区域
    img = find_text_foreground(img)
    imshow("bitwise", img)
    
    #3.把字体的轮廓放大一些
    img = cv2_dilate(img)
    imshow("zoomed", img)
    
    #4.把字体一行一行地变成长矩形条
    w1, h1 = 30, min_line_space
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(w1, h1))  
    img = get_text_area(img, w1,h1, kernel)

    imshow('font rect', img, False)
    
    #5.画出所有字体矩形的轮廓
    contours = find_text_rects(img)
    #cv2.drawContours(imsrc, contours, -1,(0,0,255),1)
    
    #测试时只取其中一个
    mycontour = contours[5]
    contours = [contours[5],]
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(imsrc, 
                      (x-rect_left_margin, y-rect_top_margin), 
                      (x+w,y+h), 
                      (100,0,255), 1)
        
    imshow('found text 111', imsrc, False)
    
    #6.需要对每个矩形按位置进行排序，再依次分割字体
    #contours = sorted(contours)
    #print '2contours = ',contours
    
    
    
    
    
    #7.对矩形框中的文字进行分割
    x,y,w,h = cv2.boundingRect(mycontour)
    print 'mycontour position in img: ',x,y,w,h
    
    rect = imsrc[y:y+h, x:x+w]
    
    print 'rect shape:',rect.shape
    
    
    imshow('rect', rect, True)
    
    verticalProjection(rect)
    
    
    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

        
    #把结果图片保存到指定路径，然后返回
    import uuid
    #tmpfile = r'F:\test\tempfiles\%s.jpg'%str(uuid.uuid4())
    tmpfile = r'E:\2kkkkk\ocr\tempfiles\%s.jpg'%str(uuid.uuid4())
    
    #cv2.imwrite(tmpfile, imsrc)
    #return tmpfile        


if __name__ == '__main__':
    get_res_img()



