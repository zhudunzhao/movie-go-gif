# _*_ coding:utf-8 _*_
#GUI模块
__author__ = "zhudu"
__date__ = "$2018-12-27 10:24:35$"

import Tkinter

class 
#主体窗口
def mainWidget():
    root = Tkinter.Tk()
    root.title('Movie to GIF')#title
    root.geometry('480x200')#widget size
    root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True
    
    #第一行
    l_file =Tkinter.Label(root,text='name').grid(row=0)
    return root

#转GIF
def toGif():
    return 