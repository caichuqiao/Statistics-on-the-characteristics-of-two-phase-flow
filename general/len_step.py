import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def px_step(px):
    if (px==np.array([0,0,0])).all():
        return 0
    if (px==np.array([0,128,0])).all():
        return 1
    if (px==np.array([0,0,128])).all():
        return 2

path0='./img/data1/000(0).png'
path1='./img_out/best1/000(0).png'
step=[]
index=[]
img0=cv2.imread(path0)
img = cv2.imread(path1)
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
for i in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    h_mean+=h/len(contours)
    y_mean+=y/len(contours)
y_mean=int(y_mean+h_mean/2)

for i in range(img.shape[1]):
    step.append(px_step(img[y_mean,i]))
    index.append(i)

plt.figure(1)
plt.subplot(3,1,1)
plt.imshow(img0)
plt.subplot(3,1,2)
plt.imshow(img)
plt.subplot(3,1,3)
plt.step(index, step)
plt.xlim(0,1280)
plt.savefig('len.png')