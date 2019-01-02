#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import Tkinter

class GIF(object):

    def __init__(self,source=None,target=None,width=0,height=0,fps=0):
        self.source=source
        self.target=target
        self.width=width
        self.height=height
        self.fps=fps

    def mainWidget(self):
        #窗体
        root = Tkinter.Tk()
        root.title('Movie to GIF')#title
        root.geometry('480x200')#widget size
        root.resizable(width=False, height=True) 
        #排版
        Tkinter.Label(root,text='选择文件').grid(row=0)

        Tkinter.Label(root,text='转换类型').grid(row=1)

        #主体循环
        root.mainloop()

    def toGif():
        return 

if __name__ == "__main__":
    g=GIF()
    g.mainWidget()
    