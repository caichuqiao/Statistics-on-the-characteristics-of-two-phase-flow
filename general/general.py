import cv2
import os
from matplotlib.lines import fillStyles
import numpy as np
import matplotlib.pyplot as plt
from process import processing
from statisticize import statistizing
from velocity import velocity_all,get_png_num

plt.style.use('ggplot')
#---------获得长度与面积分布图---------#
len_sqr=1
#-----------获得速度分布图------------#
velocity=1
#----------是否为不规则管道-----------#
#  规则管道-mode=0 不规则管道-mode=1  #
mode=0
path='C:/GraduateWork/deeplabv3-plus-pytorch/general/video/'
path_avi=os.path.join(path,'3_liq_3_gas_mid_CR600x2_1836-ST-B-062_1.avi')

avi_name=os.path.splitext(os.path.basename(path_avi))[0]
path_png=path+'%s/png/'%avi_name
path_data=path+'%s/data/'%avi_name
path_data1=path+'%s/data1/'%avi_name
path_txt=path+'%s/txt/'%avi_name

if not os.path.exists(path_png):
    os.makedirs(path_png)
if not os.path.exists(path_data):
    os.makedirs(path_data)
if not os.path.exists(path_data1):
    os.makedirs(path_data1)
if not os.path.exists(path_txt):
    os.makedirs(path_txt)

# f=open(path_txt+'mean_std.txt','w')

# # 读取视频
# cap = cv2.VideoCapture(path_avi)

# # 获取帧数
# frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(frame_count)
# # 循环读取每一帧
# for i in range(frame_count):
#     success, frame = cap.read()
#     # 保存每一帧
#     path_frame=os.path.join(path_png,"%d.png" % i)
#     cv2.imwrite(path_frame, frame)

# # os.system('python C:\GraduateWork\deeplabv3-plus-pytorch\predict.py --pathi %s --patho %s'%(path_png,path_data))
# res=os.popen('python C:/GraduateWork/deeplabv3-plus-pytorch/predict.py --pathi %s --patho %s'%(path_png,path_data))
# labels = res.read()  # 形成阻塞效果，使另一通道中程序运行完再执行下一句
# processing(path_data,path_data1,mode)

if len_sqr:
    len_liq_max,len_liq,len_gas,Area_liquid,Area_gas=statistizing(path_data1,mode)
    plt.figure('length/square')
    plt.subplot(2,1,1)
    plt.grid(True,zorder=0)
    plt.hist(len_liq,bins=5,label='liquid',color='lightcoral',edgecolor='white')
    len_liq = np.array(len_liq)
    mean0 = np.mean(len_liq)
    std0 = np.std(len_liq)
    print('liq:%d'% len(len_liq_max))
    print('gas:%d'% len(len_gas))
#     plt.hist(len_liq_max,label='liquid_max',color='royalblue',edgecolor='white')
#     len_liq_max = np.array(len_liq_max)
#     mean2 = np.mean(len_liq_max)
#     std2 = np.std(len_liq_max)

#     plt.hist(len_gas,bins=50,label='gas',color='lightseagreen',edgecolor='white')
#     len_gas = np.array(len_gas)
#     mean1 = np.mean(len_gas)
#     std1 = np.std(len_gas)

#     plt.title('length')
#     plt.xlabel('length gas/liquid(unit: um)')
#     plt.ylabel('quantitiy')
#     # plt.xlim(400,)
#     plt.legend(loc="upper left")

#     plt.subplot(2,1,2)
#     plt.grid(True,zorder=0)    
#     plt.hist(Area_liquid,label='liquid',color='lightcoral',edgecolor='white')
#     Area_liquid = np.array(Area_liquid)
#     mean3 = np.mean(Area_liquid)
#     std3=np.std(Area_liquid)
    
#     plt.hist(Area_gas, label='gas',color='lightseagreen',edgecolor='white')
#     Area_gas = np.array(Area_gas)
#     mean4 = np.mean(Area_gas)
#     std4 = np.std(Area_gas)

#     plt.title('square')
#     plt.xlabel('square gas/liquid(unit: mm*mm)')
#     plt.ylabel('quantitiy')
#     # plt.xlim(0.21,)
#     plt.tight_layout()

#     plt.legend(loc="upper left")    
#     plt.savefig(path+'%s/len&sqr.png'%avi_name)

# if velocity:
#     num=get_png_num(path_data1)
#     arr_liq,arr_gas=velocity_all(path_data1,0,num)
#     plt.figure('velocity')
#     plt.grid(True,zorder=0)    
#     plt.hist(arr_liq,bins=5,label='liquid',color='purple',edgecolor='white')
#     arr_liq = np.array(arr_liq)
#     mean5 = np.mean(arr_liq)
#     std5 = np.std(arr_liq)

#     plt.hist(arr_gas,bins=30,label='gas',color='gold',edgecolor='white')
#     arr_gas = np.array(arr_gas)
#     mean6 = np.mean(arr_gas)
#     std6 = np.std(arr_gas)

#     plt.title('velocity')
#     plt.xlabel('velocity gas/liquid(unit: m/s)')
#     plt.ylabel('quantitiy')
#     # plt.xlim(0.7,1.0)

#     plt.legend(loc="upper left")
#     plt.savefig(path+'%s/velocity.png'%avi_name)


# f.write('length\nliquid:\nmean-%e\nstd-%e\ngas:\nmean-%e\nstd-%e\nliquid_max:\nmean-%e\nstd-%e\n \
#         square\nliquid:\nmean-%e\nstd-%e\ngas:\nmean-%e\nstd-%e\n \
#         velocity\nliquid:\nmean-%e\nstd-%e\ngas:\nmean-%e\nstd-%e' \
#         %(mean0,std0,mean1,std1,mean2,std2,mean3,std3,mean4,std4,mean5,std5,mean6,std6))

# f.close()

# plt.show()