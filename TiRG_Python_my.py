#coding:utf8

"""
官方网址：http://tirg.sourceforge.net/
样例图片参考：http://funkybee.narod.ru/

目前来看，可以通过以下方式优化：
1.识别时，有时边缘会切到字体，得到实际位置时，再向外延伸点可以更加精确
2.因为大致位置还是非常精确的，所以可以再在这个位置上面搜索相同的颜色的字体等信息
3.第二步需要会swt的计算





默认行与行之间至少相隔几个像素
4.尝试用一个长 条型去依次横向与每个区域相加


"""

import time
import cv2
import Tkinter
from PIL import Image, ImageTk


def text_detector(file_name):
    #1.打开图片
    try:
        #fp = open(pic_dir + file_name, 'rb')
        fp = open(file_name, 'rb')
        io = Image.open(fp)
        io.load()
        fp.close()
    except:
        print '图片不存在 或不能读取文件!'
        return -1
    
    image = cv2.imread(file_name)
    cv2.imshow('image', image)
    
    
    #2.设置经验值
    # Needful magic numbers; mostly empiric ones:
    dw = 24 #default=24
    dh = 24 #default=24
    
    
    c_min = 35
    pl_min = 0.5
    h_min = 6
    h_max = 44
    ns_min = 2
    
    print '初始值：dw,dh',dw,dh
    
    d8 = ((1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1))
    
    w, h = io.size
    print '长：%s 高:%s' % (w,h)    
    
    #3.将图片转换成rgb格式
    im = io.convert('L')
    if io.mode != 'RGB':
        io = io.convert('RGB')
        
        
    io2 = io.copy()
    #将保存原图的所有对应像素值
    lum = [[0] * w for i in range(h)]
    nei = [[0] * w for i in range(h)]
    
    sm = 0  #sm是图片中所有像素值[0-255]的和
    
    for i in range(h):
        for j in range(w):
            lum[i][j] = im.getpixel((j, i))

            sm += lum[i][j]
            io2.putpixel((j, i), (111,111,111)) #将io2置为灰色的
       
            
            
            
    print 'sm = ',sm
    #io2.show()
    #time.sleep(10)
    
    
    #sr是所有 像素值的平均值
    sr = float(sm) / (h*w)
    
    
    #保存所有值与平均值的差值的绝对值的和
    c = 0
    for i in range(h):
        for j in range(w):
            c += abs(sr - lum[i][j])
            
    #每个值与平均值相差的平均值
    c = c/(h*w)
    c = int(0.5 + c)
    
    
    print 'sr =', sr
    print 'c =', c, 'c_min = ',c_min
    c = max(c, c_min)  
    
    print 'c的最终值：',c


    def show_res_image(r):
        "显示最终的结果图片"
        for ri in r:
            for p in range(ri[0], ri[1] + 1):
                for q in range(ri[2], ri[3] + 1):
                    t = io.getpixel((q, p))
                    if ri[4] > 0.6:
                        io2.putpixel((q, p), t)
                    else:
                        io2.putpixel((q, p), (255, 255 - t[1], 255 - t[2]))
        def btn_close(event):
            event.widget.quit()
        root = Tkinter.Tk()
        
        #root.bind("<Button>", btn_close)
        root.geometry('%dx%d'% (w, h))
        tkpi = ImageTk.PhotoImage(io2)
        lbl_image = Tkinter.Label(root, image=tkpi)
        lbl_image.place(x=0, y=0, width=w, height=h)
        root.mainloop()

    def get_nei():
        #依次循环每一行，除掉第一行和最后一行
        for i in range(1, h - 1):
            #循环第一行的第一个像素，除去第一个和最后一个像素
            for j in range(1, w - 1):
                y = 0
                t = set([])
                for k in range(8):
                    if abs(lum[i][j] - lum[i + d8[k][0]][j + d8[k][1]]) > c:
                        y += 1
                        t.add(k)
                if y in (3,):
                    if min(t) + (y - 1) == max(t) or \
                       t == set((6,7,0)) or t == set((7,0,1)):
                        nei[i][j] = y
                    else:
                        nei[i][j] = -y
                else:
                    nei[i][j] = y
        

    
    def stroke_calc(p1, q1):
        "计算笔划"
        p2 = min(h - 1, p1 + dh)
        q2 = min(w - 1, q1 + dw)
        nm = (p2 - p1) * (q2 - q1)
        u = 0.0
        x = [0] * 10
        for i in range(p1, p2):
            fl = 0
            for j in range(q1, q2):
                y = nei[i][j]
                if y >= 0:
                    x[y] += 1
                if y == 0:
                    fl += 1
            if fl == q2 - q1:
                u += 1.0
        if 0 in x[:7] or nm > (x[3] + x[6]) * 20:
            return x[9]
        cnt1 = x[3] * 16 + x[6] * 16
        cnt2 = x[0]
        x[9] = int(cnt1 * cnt2 * 1.0 / nm)
        x[9] = int(x[9] * (1 + u / (p2 - p1))**2)
        if x[9] < 600 or x[9] > 3000:
            x[9] = 0
        return x[9]


    def get_text_regions():
        "找出文字区域"
        ww = w / dw
        hh = h / dh
        print 'w, h, dw, dh: ',w,h,dw,dh
        print 'ww = %s, hh = %s ' % (ww,hh)
        
        #构造出一个list，元素个数为h+1个，每个元素包含w+3个零
        b = [[0] * (w + 3) for i in range(h + 1)]
        #print '-wen-: b = ',b
        
        #循环12次
        for dy in (0, dh / 2): 
            m = [[0] * (ww + 3) for i in range(hh + 1)]
            
            for i in range(1 + dy, h, dh):
                for j in range(1, w, dw):
                    m[(i - 1 - dy) / dh][(j - 1) / dw] = stroke_calc(i, j)
                    
                    
            for i in range(hh + 1):
                for j in range(ww):
                    if m[i][j] != 0 and m[i][j + 1] != 0 and m[i][j + 2] != 0 and \
                        m[i][j] + m[i][j + 1] + m[i][j + 2] > 3 * 800:
                        m[i][ww + 2] = 1
                        break
                    
                    
            for i in range(hh + 1):
                if m[i][ww + 2] == 0:
                    continue
                for j in range(ww + 1):
                    if m[i][j] != 0:
                        h1 = i * dh + 1 + dy
                        h2 = h1 + dh
                        h2 = min(h - 1, h2)
                        w1 = j * dw + 1
                        w2 = w1 + dw
                        w2 = min(w - 1, w2)
                        for p in range(h1, h2):
                            b[p][w + 2] = 1
                            for q in range(w1, w2):
                                if nei[p][q] != 0:
                                    b[p][q] = 1
        step = 60
        for i in range(h):
            if b[i][w + 2] != 0:
                j = 0
                cnt = 0
                while j <= w - step:
                    if b[i][j] != 0 and b[i][j + 1] != 0 and b[i][j + 2] != 0:
                        sm = sum(b[i][j:j + step])
                        if sm > step * 0.4:
                            for k in range(j, j + step):
                                b[i][k] += 2
                            cnt += 1
                            j += step
                        else:
                            j += 1
                    else:
                        j += 1
                if cnt == 0:
                    b[i] = [0] * (w + 3)
                else:
                    b[i][w + 2] = cnt
        cnt = 0
        for i in range(h + 1):
            if b[i][w + 2] == 0:
                if cnt > 0 and cnt < 8:
                    for ii in range(i - cnt, i):
                        b[ii] = [0] * (w + 3)
                cnt = 0
            else:
                cnt += 1
        r = []
        for i in range(h):
            for j in range(w):
                if b[i][j] > 1:
                    cnt = 1
                    x1 = w
                    x2 = 0
                    y1 = h
                    y2 = 0
                    b[i][j] *= -1
                    v = [[i, j]]
                    while len(v) != 0:
                        ww = []
                        for vv in v:
                            for k in range(8):
                                yy = vv[0] + d8[k][0]
                                xx = vv[1] + d8[k][1]
                                if xx < 0 or xx >= w or yy < 0 or yy >= h:
                                    continue
                                if b[yy][xx] > 1:
                                    b[yy][xx] *= -1
                                    ww += [[yy, xx]]
                                    x1 = min(x1, xx)
                                    x2 = max(x2, xx)
                                    y1 = min(y1, yy)
                                    y2 = max(y2, yy)
                        v = ww[:]
                        cnt += len(v)
                    dx = x2 - x1 + 1
                    dy = y2 - y1 + 1
                    pl = cnt * 1.0 / dx / dy
                    if pl > pl_min and dy > h_min and dy < h_max and dx > dy * ns_min:
                        r += [[y1, y2, x1, x2, pl]]
        return r

    get_nei()
    
    ans = get_text_regions()
    
    if len(ans) == 0:
        print 'No text detected...\n'
        return 0
    print len(ans), 'text(-like) region(s) detected!\n'
    print '找到的区域 ans = ', ans
    show_res_image(ans)
    return 1



if __name__ == '__main__':
    f = ['img/small_chi.png',
         'img/s.jpg',
         r'F:\test\word_with_img\wiki.jpg',
         r'F:\test\word_with_img\bigfont.png',
         r'F:\test\word_with_img\wiki2.jpg',
         'img/222t.jpg',
         'img/eng1.png', 
         'img/u.jpg']
    fn = f[3]
    ret = text_detector(fn)    
    
    
