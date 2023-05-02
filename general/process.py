import cv2
import os
import numpy as np

def filter1(hierarchy,contours,img,color):
    i=0
    while i!=-1:
        if hierarchy[0][i][2]!=-1:         
            area=cv2.contourArea(contours[i])
            area0=0
            a=hierarchy[0][i][2]
            while a!=-1:
                area0+=cv2.contourArea(contours[a])
                cv2.drawContours(img, contours, a, color, cv2.FILLED)
                a=hierarchy[0][a][0]
            if area0/area>0.015:
                cv2.drawContours(img, contours, i, (0,0,0), cv2.FILLED)
        i=hierarchy[0][i][0]

def filter2(hierarchy,contours,ps,img,mode):
    #ps_liquid=0.6
    #ps_gas=0.8
    for i in range(len(contours)):
        if hierarchy[0][i][3]==-1:
            x, y, w, h = cv2.boundingRect(contours[i])
            if mode==0:
                area = cv2.contourArea(contours[i])
                p=area/(w*h)
                if p<ps:
                    cv2.drawContours(img, contours, i, (0,0,0), cv2.FILLED)
            if h<100 or w<100 or x<=5 or x+w>=1275: 
                cv2.drawContours(img, contours, i, (0,0,0), cv2.FILLED)

def filter3(hierarchy,contours,np,img):
    #np_liquid=24
    #np_gas=20
    for i in range(len(contours)):
        if hierarchy[0][i][3]==-1:        
            peri = cv2.arcLength(contours[i],True)
            approx = cv2.approxPolyDP(contours[i],0.005*peri,True)
        if len(approx)>=np:
            cv2.drawContours(img, contours, i, (0,0,0), cv2.FILLED)





def processing(path1,path2,mode):
    files = os.listdir(path1)
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

        contours0, hierarchy0 = cv2.findContours(gray_img0, cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
        contours1, hierarchy1 = cv2.findContours(gray_img1, cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
        contours=contours0+contours1

        # filter1(hierarchy0,contours0,img,(0, 0, 128))
        # filter1(hierarchy1,contours1,img,(0, 128, 0))

        filter2(hierarchy0,contours0,0.6,img,mode)
        filter2(hierarchy1,contours1,0.8,img,mode)

        # if mode==1:
        #     filter3(hierarchy0,contours0,24,img)
        #     filter3(hierarchy1,contours1,20,img)

        cv2.imwrite(path2+file, img)

path1="C:/GraduateWork/deeplabv3-plus-pytorch/img_out/best3/" # folder input
path2="C:/GraduateWork/deeplabv3-plus-pytorch/img_out/best3/" #folder output
processing(path1,path2,1)