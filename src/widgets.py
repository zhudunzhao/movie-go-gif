#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import Tkinter as tk
# 弹出
import tkMessageBox as mb
import tkFileDialog as td
import re #正则


class Application(tk.Frame):

    def __init__(self,master=None,source='',target='',height=600,width=800,fps=60):
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
        # 初始化字段
        source=tk.StringVar()
        target=tk.StringVar()
        width=tk.StringVar()
        height=tk.StringVar()
        fps=tk.StringVar()

        # 第一行(选择文件)
        tk.Label(self,text='选择文件:').grid(row=0)
        self.getsource=tk.Entry(self,textvariable=source).grid(row=0,column=1,columnspan=2,sticky=tk.E+tk.W)
        tk.Button(self, text = "路径选择", command = self.selectPath).grid(row = 0, column = 3,sticky=tk.E+tk.W)
        #第二行（高宽）
        tk.Label(self,text='尺寸:').grid(row=1)
        tk.Entry(self,textvariable=width).grid(row=1,column=1,sticky=tk.E)
        tk.Entry(self,textvariable=height).grid(row=1,column=2,sticky=tk.E)
        # 第三行（fps）
        tk.Label(self,text='fps:').grid(row=2)
        tk.Entry(self,textvariable=fps).grid(row=2,column=1,columnspan=2,sticky=tk.E+tk.W)
        #第四行(保存路径)
        tk.Label(self,text='保存路径:').grid(row=3)
        tk.Entry(self,textvariable=target).grid(row=3,column=1,columnspan=2,sticky=tk.E+tk.W)
        tk.Button(self, text = "路径选择", command = self.savePath).grid(row = 3, column = 3,sticky=tk.E+tk.W)
        #第四行(保存按钮)
        tk.Button(self, text = "路径选择", command = self.done).grid(row = 4,column=1, columnspan = 2,sticky=tk.E+tk.W)

        #设置默认值
        source.set(self.source)
        target.set(self.target)
        fps.set(self.fps)
        width.set(self.width)
        height.set(self.height)
        print self.fps

        
    # 提交处理
    def done(self):
        source=self.getsource.get()
        print source

    #选择文件
    def selectPath(self):

        self.file_opt = options = {}
        options['filetypes'] = [('视频文件', '*.mp4;*.swf;*.avi;*.wma;*.rm;*.mov'),('所有文件', '.*')]
        options['title'] = '选择视频文件'

        path_ = td.askopenfilename(**self.file_opt)
        self.source.set(path_)
    # 保存路径
    def savePath(self):
        self.dir_opt = options = {}
        options['filetypes'] = [('GIF', '.gif')]
        options['title'] = 'GIF保存名称'
        options['initialfile']='output'

        path_=td.asksaveasfilename(**self.dir_opt)
        self.target.set(path_)
    #检测组件
    def is_ffmpeg(self):
        mb.showinfo("welcome","Welcome Message")
    

if __name__ == "__main__":
    # 创建一个Application对象app
    app = Application()
    # 设置窗口标题为'Movie to GIF'
    app.master.title('Movie to GIF')
    # 设置默认值
    app.fps=1000
    # 主循环开始
    app.mainloop()
    