# Statistics-on-the-characteristics-of-two-phase-flow
A programm package based on deeplabv3+ neural network for statistical characteristics of gas-liquid two-phase flow written in python.
## related repository
The parameters used in the code are based on the experimental results of semantic segmentation of gas-liquid two-phase flow using the deeplabv3+ neural network. 
The link of source code of deeplabv3+ I used as follows：
[deeplabv3+](https://github.com/bubbliiiing/deeplabv3-plus-pytorch)
The link of the weight file as follows:
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
