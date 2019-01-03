#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import Tkinter as tk
# 弹出
import tkMessageBox as mb
import tkFileDialog as td
import re #正则


class Application(tk.Frame):

    def __init__(self,master=None,source=None,target=None,width=0,height=0,fps=0):
        tk.Frame.__init__(self,master)
        # 参数
        self.source=source
        self.target=target
        self.width=width
        self.height=height
        self.fps=fps
        # 显示窗口，并使用grid布局
        self.grid(row=0)
        # 创建控件
        self.main()
        
   
    # 布局
    def main(self):
        # 第一行
        tk.Label(self,text='选择文件').grid(row=0)
        tk.Entry(self,textvariable=self.source).grid(row=0,column=1,columnspan=2,sticky=tk.E+tk.W)
        tk.Button(self, text = "路径选择", command = self.selectPath).grid(row = 0, column = 3,sticky=tk.E+tk.W)
        #第二行
        tk.Label(self,text='尺寸').grid(row=1)
        tk.Entry(self,textvariable=self.source).grid(row=1,column=1,sticky=tk.E)
        tk.Entry(self,textvariable=self.source).grid(row=1,column=2,sticky=tk.E)
        # 第三行
       

    #选择文件
    def selectPath(self):
        path_ = td.askopenfilename()
        print path_

    def is_ffmpeg(self):
        mb.showinfo("welcome","Welcome Message")
    

if __name__ == "__main__":
    # 创建一个Application对象app
    app = Application()
    # 设置窗口标题为'Movie to GIF'
    app.master.title('Movie to GIF')
    # 主循环开始
    app.mainloop()
    