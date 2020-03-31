#导入必要的库
import tkinter
import datetime                                     #供插入时间日期用
import matplotlib.pyplot as plt                     #供绘制词频图使用
import numpy as np
import webbrowser                                  #供打开网页使用
from tkinter.filedialog import askopenfilename    #供打开文件使用
from tkinter import ttk                             #供构建下拉框使用
from pylab import mpl                              #供显示中文与负号使用
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
#源文件处理
Liststop=[]
Article=[]
Wordlist=[]
Way=[]
def turnon():
    root=tkinter.Tk()
    def selectPath():
        path_ = askopenfilename()
        path.set(path_)
        Way.append(path.get())
        print('你要打开的文件位置为：',Way[0])
        root.destroy()
        deal()
    path = tkinter.StringVar()
    tkinter.Label(root,text = "txt目标路径:").grid(row = 0, column = 0)
    tkinter.Entry(root, textvariable = path).grid(row = 0, column = 1)
    tkinter.Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
    root.mainloop()

def deal():
    f=open(Way[0])
    article=f.read()
    g=open('停用词表.txt')
    Liststop.append(g.read())
    punc=[',','.',':','"','(',')','!','—','?','/','^','--']
    for i in punc:
        article=article.replace(i,' ')
    article=article.lower()
    #print(article)
    wordlist=article.split()
    Wordlist.append(wordlist)
    Article.append(article)
    textbox.insert(1.0,article)
#实现各种功能的函数

#开始模块
def close():
    top.destroy()
#插入模块
def timeinsert():           #插入时间
    now=datetime.datetime.now()
   # print (now.strftime('%Y-%m-%d'))
    textbox.mark_set('mark',tkinter.END)
    textbox.insert('mark','\n                        ')
    textbox.insert('mark',now.strftime('%Y-%m-%d'))
Aut=[]
def authorinsert():         #插入作者
    aut=tkinter.Tk()
    aut.title('作者')
    def addname():
        Aut.append(b.get())
        textbox.mark_set('mark',1.0)
        textbox.insert('mark',' '*(35-len(Aut[0]))+Aut[0]+'\n')
        aut.destroy()
    tkinter.Label(aut,text='请输入作者名字：').grid(row = 0, column = 0)
    b=tkinter.Entry(aut)
    b.grid(row = 0, column = 1)
    tkinter.Button(aut,command=addname,text='确认').grid(row=0,column=2)
    aut.mainloop()

TIT=[]
def titinsert():         #插入题目
    tit=tkinter.Tk()
    tit.title('题目')
    def addtit():
        TIT.append(c.get())
        textbox.mark_set('mark',1.0)
        textbox.insert('mark',' '*((45-len(TIT[0]))//2)+TIT[0]+'\n')
        tit.destroy()
    tkinter.Label(tit,text='请输入题目：').grid(row = 0, column = 0)
    c=tkinter.Entry(tit)
    c.grid(row = 0, column = 1)
    tkinter.Button(tit,command=addtit,text='确认').grid(row=0,column=2)
    tit.mainloop()

#审阅模块