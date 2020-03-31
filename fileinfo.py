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
Num=[]
def sum_fraquency():        #词频统计
    worddict={}
    for j in Wordlist[0]:
        if j in worddict:
            worddict[j]+=1
        else:
            worddict[j]=1
    Num.append(len(worddict))
    return worddict
def num():
    ab=sum_fraquency()
    print('总词数为'+str(Num[0]))
def rank():                  #关键词统计
    useword={}
    worddict=sum_fraquency()
    for key in worddict:
        if key in Liststop[0]:
            continue
        else:
            useword[key]=worddict[key]
    orderword=sorted(useword.items(),key=lambda d:d[1],reverse=True)
    print('关键词为：',orderword[0:6])
    return orderword[0:6]

def draft():                 #绘制词频图
    orderword=rank()
    word=[]
    fluency=[]
    for i in orderword:
        word.append(i[0])
        fluency.append(i[1])
    plt.figure(figsize=(9,6))
    idx = np.arange(6)
    width=0.5
    plt.bar(idx,fluency,width, color='red')
    plt.xlabel('单词')
    plt.ylabel('词频')
    plt.xticks(idx+width/2,word)
    plt.show()

Find=[]
def finds():                     #查找功能
    def finding():
        Find.append(a.get())
      #  print(Find)
        if Find[0] in Article[0]:
            weizhi=Article[0].index(Find[0])
            hang=weizhi//45
            lie=weizhi%45
            print('在第'+str(hang+1)+'行,第'+str(lie)+'列')
        else:
            print('没有找到！')
        find.destroy()
    find=tkinter.Tk()
    find.title('查找')
    tkinter.Label(find,text='请输入要查找的内容').grid(row = 0, column = 0)
    a=tkinter.Entry(find)
    a.grid(row = 0, column = 1)
    tkinter.Button(find,text='确认查找',command=finding).grid(row=0,column=2)
    find.mainloop()
    
#查看帮助模块
def helpyou():  
    webbrowser.open('大作业答辩.pptx')
top=tkinter.Tk()
frame=tkinter.Frame(height=20,width=20)
frame.pack() 
textbox=tkinter.Text(top,width=45,height=15,font=48)
textbox.pack()
label1=tkinter.Label(frame,text='开始',fg='blue',font=("黑体", 10,"normal")).grid(row=0,column=0)
label2=tkinter.Label(frame,text='插入',fg='blue',font=("黑体", 10,"normal")).grid(row=1,column=0)
label3=tkinter.Label(frame,text='审阅',fg='blue',font=("黑体", 10,"normal")).grid(row=2,column=0)
label4=tkinter.Label(frame,text='查找',fg='blue',font=("黑体", 10,"normal")).grid(row=3,column=0)
button1=tkinter.Button(frame,text=' 查看关键词 ',command=rank,font=("微软雅黑", 9,"normal")).grid(row = 2, column = 3)
button2=tkinter.Button(frame,text='插入当前日期',command=timeinsert,font=("微软雅黑", 9,"normal")).grid(row = 1, column = 3)
button3=tkinter.Button(frame,text=' 绘制词频图',command=draft,font=("微软雅黑", 9,"normal")).grid(row = 2, column = 4)
button4=tkinter.Button(frame,text='  查看帮助  ',command=helpyou,font=("微软雅黑", 9,"normal")).grid(row = 0, column = 4)
button5=tkinter.Button(frame,text='    退出    ',command=close,font=("微软雅黑", 9,"normal")).grid(row = 0, column = 5)
button6=tkinter.Button(frame,text='    查找    ',command=finds,font=("微软雅黑", 9,"normal")).grid(row = 3, column = 3)
button7=tkinter.Button(frame,text='  插入作者  ',command=authorinsert,font=("微软雅黑", 9,"normal")).grid(row = 1, column =4)
button8=tkinter.Button(frame,text='  插入题目  ',command=titinsert,font=("微软雅黑", 9,"normal")).grid(row = 1, column =5)
button9=tkinter.Button(frame,text=' 查看总词数 ',command=num,font=("微软雅黑", 9,"normal")).grid(row = 2, column =5 )
button10=tkinter.Button(frame,text='    打开     ',command=turnon,font=("微软雅黑", 9,"normal")).grid(row = 0, column = 3)

top.mainloop()
