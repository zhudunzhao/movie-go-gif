#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import tkinter as tk
from tkinter import ttk #ttk新gui
import tkinter.messagebox as mb #弹窗库
import tkinter.filedialog as td  #选择器
from tkinter import scrolledtext #滚动
import re #正则
import os
from ffmpy import FFmpeg as ff


class Application(ttk.Frame):

    def __init__(self,master=None,source='',target='',height=600,width=800,fps=60):
        ttk.Frame.__init__(self,master)
        # 参数
        self.source=tk.StringVar()
        self.target=tk.StringVar()
        self.width=tk.StringVar()
        self.height=tk.StringVar()
        self.fps=tk.StringVar()
        #设置
        self.source.set(source)
        self.target.set(target)
        self.width.set(width)
        self.height.set(height)
        self.fps.set(fps)
 
        
        # 显示窗口，并使用grid布局
        self.grid(row=0)
        # self.grid_propagate(0)
        
        # 创建控件
        self.main()
        
        
   
    # 布局
    def main(self):

        # 第一行(选择文件)
        ttk.Label(self,text='选择文件:').grid(row=0)
        self.getsource=ttk.Entry(self,textvariable=self.source)
        self.getsource.grid(row=0,column=1,columnspan=2,sticky=tk.E+tk.W)
        ttk.Button(self, text = "路径选择", command = self.selectPath).grid(row = 0, column = 3,sticky=tk.E+tk.W)
        #第二行（高宽）
        ttk.Label(self,text='尺寸:').grid(row=1)
        ttk.Entry(self,textvariable=self.width).grid(row=1,column=1,sticky=tk.E+tk.W)
        ttk.Entry(self,textvariable=self.height).grid(row=1,column=2,sticky=tk.E+tk.W)
        # 第三行（fps）
        ttk.Label(self,text='fps:').grid(row=2)
        ttk.Entry(self,textvariable=self.fps).grid(row=2,column=1,columnspan=2,sticky=tk.E+tk.W)
        #第四行(保存路径)
        ttk.Label(self,text='保存路径:').grid(row=3)
        ttk.Entry(self,textvariable=self.target).grid(row=3,column=1,columnspan=2,sticky=tk.E+tk.W)
        ttk.Button(self, text = "路径选择", command = self.savePath).grid(row = 3, column = 3,sticky=tk.E+tk.W)
        #第四行(保存按钮)
        ttk.Button(self, text = "生成", command = self.done).grid(row = 4,column=1, columnspan = 2,sticky=tk.E+tk.W)

        #第五行（信息输出区）
        ttk.Label(self,text='信息输出:').grid(row=5,sticky=tk.W)
        self.scr=scrolledtext.ScrolledText(self,height=10 ,wrap=tk.WORD)
        self.scr.grid(column=0, row=6, sticky='WE', columnspan=4)
         

        
    # 提交处理
    def done(self):
        
        
        

        result = os.popen('ffmpeg -version')
        res = result.read()
        for line in res.splitlines():
                #mb.showinfo('提示',line)
                self.scr.insert(tk.END, str(line)+'\n')
                
        self.scr.insert(tk.END, str('==========完成=====================================')+'\n')
        self.scr.see(tk.END)

    #安装ffmpeg
    def installFF(self):
        pass

    #运行生成命令
    def runGif(self):
        #生成画版
        self.scr.insert(tk.END, str('===生成画版=====================================')+'\n')
        cmd1='ffmpeg -i '+User+' -vf fps='+fps+',scale='+Width+':'+height+':flags=lanczos,palettegen -y '+randmo+'.png'
        
        #生成gif


    #选择文件
    def selectPath(self):

        self.file_opt = options = {}
        #options['filetypes'] = [('视频文件', '*.mp4;*.swf;*.avi;*.wma;*.rm;*.mov'),('所有文件', '.*')]
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
        pass
    

if __name__ == "__main__":
    # 创建一个Application对象app
    app = Application()
    # 设置窗口标题为'Movie to GIF'
    app.master.title('Movie to GIF')


    # 主循环开始
    app.mainloop()
    