# Statistics-on-the-characteristics-of-two-phase-flow
A programm package based on deeplabv3+ neural network for statistical characteristics of gas-liquid two-phase flow written in python.
## Related repository
The parameters used in the code are based on the experimental results of semantic segmentation of gas-liquid two-phase flow using the deeplabv3+ neural network.   
The link of source code of deeplabv3+ I used：
[deeplabv3+](https://github.com/bubbliiiing/deeplabv3-plus-pytorch)   
The link of the weight file:
[Weight file](https://drive.google.com/file/d/1YD-unu-BO5ZAAszYWBkj8oB8G-iTN72o/view?usp=share_link)   
Remember to modify the parameters in the neural network,
```
name_classes = ["background","liquid","gas"]
```
where gas corresponds to green color, and liquid corresponds to red color.
## Configuration Environment
You can configure the environment required to run the program through the following commands.
```
pip install -r requirements.txt
```
## Parameters need to be aware of
In file general.py:
```
#---------Get length and area distribution diagram---------#
len_sqr=1
#-----------Get the speed distribution map ------------#
velocity=1
#----------Whether it is a variable cross-section microchannel -----------#
#Constant cross-section microchannel-mode=0 Variable cross-section microchannel-mode=1#
mode=0
#---------Path where stores the video-------#
path='C:/GraduateWork/deeplabv3-plus-pytorch/general/video/'
#---------The name of video file(for example: 3_liq_3_gas_mid_CR600x2_1836-ST-B-062_1.avi)----------#
path_avi=os.path.join(path,'3_liq_3_gas_mid_CR600x2_1836-ST-B-062_1.avi')   
#------------------------------------------------------------------------------------------------------------------------#
#---------Change the path C:/GraduateWork/deeplabv3-plus-pytorch/predict.py into yourselfs-------#
res=os.popen('python C:/GraduateWork/deeplabv3-plus-pytorch/predict.py --pathi %s --patho %s'%(path_png,path_data))
```
If you have followed the instructions above, please just run general.py directly.
## Achievements
Example of the original video of gas-liquid two-phase flow:   
<div align=center><img width="3000" src="https://github.com/caichuqiao/Statistics-on-the-characteristics-of-two-phase-flow/blob/main/pic/0i.png"/></div>  
Example of the processed video of gas-liquid two-phase flow:   
<div align=center><img width="3000" src="https://github.com/caichuqiao/Statistics-on-the-characteristics-of-two-phase-flow/blob/main/pic/0.png"/></div>  
Distribution diagram of length and area of gas-liquid two-phase flow gived by programm:   
Distribution diagram of veolocity of gas-liquid two-phase flow gived by programm:   
