#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import Tkinter as tk
# 弹出
import tkMessageBox as mb
import tkFileDialog 
import re #正则


class GIF(object):

    def __init__(self,source=None,target=None,width=0,height=0,fps=0):
        self.source=source
        self.target=target
        self.width=width
        self.height=height
        self.fps=fps

        # mb.showinfo("welcome","Welcome Message")

    # 窗体
    def widget(self):
        root = tk.Tk()
        root.title('Movie to GIF')#title
        root.geometry('480x200')#widget size
        root.resizable(width=False, height=True) 
        return root

    # 布局
    def main(self):
        root=self.widget()
        #第一行
        tk.Label(root,text='选择文件').grid(row=0)
        Button(root, text = "路径选择", command = self.selectPath).grid(row = 0, column = 2,sticky=E+W)
        #第二行
        tk.Label(root,text='转换类型').grid(row=1)

        #主体循环
        root.mainloop()

    #选择文件
    def selectPath():
        path_ = tkFileDialog.askopenfilename(filetypes=[("bmp格式".decode('gbk'),"py")])

    def toGif():
        return 

if __name__ == "__main__":
    g=GIF()
    g.main()
    