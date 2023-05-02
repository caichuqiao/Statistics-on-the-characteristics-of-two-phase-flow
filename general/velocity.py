import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# 获取指定文件夹下的png文件数量
def get_png_num(path):
    # 定义一个变量，用来记录文件数量
    num = 0
    # 遍历文件夹下的所有文件
    for root, dirs, files in os.walk(path):
        for file in files:
            # 判断文件是否为png文件
            if os.path.splitext(file)[1] == '.png':
                num += 1
    return num

def map_len(path1,a,b):
    # path1='./img_out/best1/' # folder input
    # num=get_png_num(path1)

    arr00=np.array([])
    arr01=np.array([])
    arr10=np.array([])
    arr11=np.array([])

    arr_liq=np.array([])
    arr_gas=np.array([])

    h_all=0
    num_cont=0

    for n in range(a,b):
        path2=os.path.join(path1,str(n)+'.png')
        img = cv2.imread(path2)
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

        for i in range(len(contours0)):
            x, y, w, h = cv2.boundingRect(contours0[i]) 
            h_all+=h
            num_cont+=1            
            if i==0:
                arr10=np.array([[x]])
            else:        
                arr10=np.append(arr10,[[x]],axis=0)   

        for i in range(len(contours1)):
            x, y, w, h = cv2.boundingRect(contours1[i])
            # h_all+=h
            # num_cont+=1 
            if i==0:
                arr11=np.array([[x]])   
            else:
                arr11=np.append(arr11,[[x]],axis=0)    

        if n!=0:
            if len(arr00)!=0 and len(arr10)!=0:
                arr_liq=np.concatenate((arr_liq, cdist(arr00,arr10).ravel()),axis=0)
            if len(arr01)!=0 and len(arr11)!=0:
                arr_gas=np.concatenate((arr_gas, cdist(arr01,arr11).ravel()),axis=0)

        arr00=arr10
        arr01=arr11
        arr10=np.array([])
        arr11=np.array([])
    h_mean=0.8/(h_all/num_cont)#(2000*400)
    return arr_liq,arr_gas,h_mean

def velocity_all(path1,a,b): 
    arr_liq,arr_gas,h_mean=map_len(path1,a,b) 
    arr_liq = np.extract((arr_liq>0)&(arr_liq<=200), arr_liq) 
    arr_gas = np.extract((arr_gas>0)&(arr_gas<=200), arr_gas) 
    arr_liq = np.multiply(arr_liq, h_mean)
    arr_gas = np.multiply(arr_gas, h_mean)
    # arr_all=np.concatenate((arr_liq, arr_gas),axis=0)
    return arr_liq,arr_gas

# arr_all=velocity_all('./img_out/best1/',1,6)
# plt.figure(1)
# plt.hist(arr_all, bins=20,color='purple')
# plt.xlabel('velocity gas/liquid(unit: [x10^4 um/s])')
# plt.ylabel('quantitiy')

# plt.figure(1)
# plt.subplot(3,2,1)
# arr_liq,arr_gas=map_len(1,6)
# plt.hist(arr_liq, bins=500,color='red')
# plt.hist(arr_gas, bins=500,color='green')
# plt.xlim(0,200)

# plt.subplot(3,2,2)
# arr_liq,arr_gas=map_len(6,12)
# plt.hist(arr_liq, bins=500,color='red')
# plt.hist(arr_gas, bins=500,color='green')
# plt.xlim(0,200)

# plt.subplot(3,2,3)
# arr_liq,arr_gas=map_len(12,18)
# plt.hist(arr_liq, bins=500,color='red')
# plt.hist(arr_gas, bins=500,color='green')
# plt.xlim(0,200)

# plt.subplot(3,2,4)
# arr_liq,arr_gas=map_len(18,24)
# plt.hist(arr_liq, bins=500,color='red')
# plt.hist(arr_gas, bins=500,color='green')
# plt.xlim(0,200)

# plt.subplot(3,2,5)
# arr_liq,arr_gas=map_len(24,30)
# plt.hist(arr_liq, bins=500,color='red')
# plt.hist(arr_gas, bins=500,color='green')
# plt.xlim(0,200)

# plt.subplot(3,2,6)
# arr_liq,arr_gas=map_len(30,36)
# plt.hist(arr_liq, bins=500,color='red')
# plt.hist(arr_gas, bins=500,color='green')
# plt.xlim(0,200)
# plt.savefig('./img_out/data/velocity_all.png')
# plt.show()