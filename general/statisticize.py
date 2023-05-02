import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def px_to_um(px,p_h):
    return px * p_h

def px_to_um2(pixel_area,p_h):
    return pixel_area * p_h * p_h


def statistizing(path1,mode):
    #------------初始化-------------#
    len_liq=[]
    len_liq_max=[]
    len_gas=[]
    Area_liquid=[]
    Area_gas=[]
    i_liq=-1
    i_gas=-1
    p_upon=0
    #------------------------------#

    # path1='./img_out/best1/' # folder input
    files = os.listdir(path1)
    # f1=open('./img_out/data1/liquid.txt','w')
    # f2=open('./img_out/data1/gas.txt','w')
    for file in files:
        img = cv2.imread(path1+file)
        # cv2.imshow("img", img)
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#HSV空间

        lower_blue=np.array([110,100,100])#blue
        upper_blue=np.array([130,255,255])

        lower_green=np.array([60,100,100])#green
        upper_green=np.array([70,255,255])

        lower_red=np.array([0,100,100])#red
        upper_red=np.array([10,255,255])

        red_mask=cv2.inRange(hsv,lower_red,upper_red)#取红色
        # blue_mask=cv2.inRange(hsv,lower_blue,upper_blue)#蓝色
        green_mask=cv2.inRange(hsv,lower_green,upper_green)#绿色

        red=cv2.bitwise_and(img,img,mask=red_mask)#对原图像处理
        green=cv2.bitwise_and(img,img,mask=green_mask)
        # blue=cv2.bitwise_and(img,img,mask=blue_mask)

        res0=red
        res1=green
        gray_img0 = cv2.cvtColor(res0, cv2.COLOR_BGR2GRAY)
        gray_img1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)

        contours0, hierarchy0 = cv2.findContours(gray_img0, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
        contours1, hierarchy1 = cv2.findContours(gray_img1, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
        contours=contours0+contours1

        h_mean=0
        y_mean=0

        if mode:
            for i in range(len(contours0)):
                x, y, w, h = cv2.boundingRect(contours0[i])
                h_mean+=h/len(contours0)
                y_mean+=y/len(contours0)
            y_mean=int(y_mean+h_mean/2)
        else:
            for i in range(len(contours)):
                x, y, w, h = cv2.boundingRect(contours[i])
                h_mean+=h/len(contours)
                y_mean+=y/len(contours)
            y_mean=int(y_mean+h_mean/2)

        for i in range(img.shape[1]):
            if (img[y_mean,i]==np.array([0,128,0])).all():
                len_gas[i_gas]+=1
            if (img[y_mean,i]==np.array([0,0,128])).all():
                len_liq[i_liq]+=1       
        
            if i<img.shape[1]-1 and (img[y_mean,i]!=img[y_mean,i+1]).any():
                if (img[y_mean,i+1]==np.array([0,128,0])).all():
                    i_gas+=1
                    len_gas.append(0)
                if (img[y_mean,i+1]==np.array([0,0,128])).all():
                    i_liq+=1
                    len_liq.append(0)         

        for i in range(len(contours0)):
            x, y, w, h = cv2.boundingRect(contours0[i])
            len_liq_max.append(w)
            area= cv2.contourArea(contours0[i])
            Area_liquid.append(px_to_um2(area,0.4/h_mean))
            # f1.write('index:{} square:{}'.format(num_liquid, px_to_mm2(area)))

        for i in range(len(contours1)):
            area= cv2.contourArea(contours1[i])
            Area_gas.append(px_to_um2(area,0.4/h_mean))
            # f2.write('index:{} square:{}'.format(num_gas, px_to_mm2(area)))

    for i in range(len(len_gas)):
        len_gas[i]=px_to_um(len_gas[i],400/h_mean)
    for i in range(len(len_liq)):
        len_liq[i]=px_to_um(len_liq[i],400/h_mean) 
    for i in range(len(len_liq_max)):
        len_liq_max[i]=px_to_um(len_liq_max[i],400/h_mean)    

    return len_liq_max,len_liq,len_gas,Area_liquid,Area_gas

# len_liq,len_gas,Area_liquid,Area_gas=statistizing('./img_out/best1/')
# plt.figure(1)
# plt.subplot(2,1,1)
# plt.hist(len_liq, bins=100,color='red')
# plt.hist(len_gas, bins=100,color='green')

# plt.subplot(2,1,2)
# plt.hist(Area_liquid, bins=100,color='red')
# plt.hist(Area_gas, bins=100,color='green')
# plt.show()
    


