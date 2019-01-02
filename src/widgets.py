#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "zhudu"
__date__ = "$2018-12-27 10:24:35$"

import Tkinter

class widgets():
    
    
    def mainWidget():
    root = Tkinter.Tk()
    root.title('Movie to GIF')#title
    root.geometry('480x200')#widget size
    root.resizable(width=False, height=True) 
    
    l_file =Tkinter.Label(root,text='name').grid(row=0)
    return root

    def toGif():
        return 




