#coding:UTF-8

import tkinter as tk
from future.moves.tkinter import filedialog
from tkinter import Variable
import numpy as np
import CryptorOfNumberFile as c
import TxtOfNumber as TN

def open_file():#打开文件，读取路径
    FilePath.set(filedialog.askopenfilename())

def transform():
    print(Password.get())
    if OperationChoice.get()==1:
        c.Encrypte(FileContent.get(),FilePath.get())
    else:
        c.Decrypte(FileContent.get(),FilePath.get())                

root = tk.Tk()#创建窗口
root.title("DES")

#左边的frame存放选择文件的按钮
FileFrame = tk.Frame(root)
FileFrame.pack(side = tk.LEFT)

Introduction = tk.StringVar()#提示选择文件
Introduction.set("请选择你要转换的文件")
IntroductionLabel = tk.Label(FileFrame, textvariable = Introduction,font = 'Helvetica -15')
IntroductionLabel.pack(side = tk.TOP)

FilePath = tk.StringVar()#展示选择文件的目录
FilePath.set("")
ShowPathLabel = tk.Label(FileFrame, textvariable = FilePath, font = 'Helvetica -15')
ShowPathLabel.pack()

OpenFile = tk.Button(FileFrame, text = "选择文件",fg = "black", command = open_file)#选择文件的按钮
OpenFile.pack(side = tk.BOTTOM)


#中间的frame存放选择
ChooseFrame = tk.Frame(root)
ChooseFrame.pack()

OperationChoice = tk.IntVar()#选择操作类别
OperationFrame = tk.LabelFrame(ChooseFrame,text = '选择你要执行的操作', font = 'Helvetica -15')
OperationFrame.pack(side = tk.LEFT)
ChooseOperation = tk.Radiobutton(OperationFrame, variable = OperationChoice, text = "加密", font = 'Helvetica -15', value = 1).pack(side = tk.TOP)
ChooseOperation = tk.Radiobutton(OperationFrame, variable = OperationChoice, text = "解密", font = 'Helvetica -15', value = 2).pack()

TypeChoice = tk.IntVar()#选择转换文件
TypeFrame = tk.LabelFrame(ChooseFrame, text = '选择转换的文件类型', font = 'Helvetica -15')
TypeFrame.pack(side = tk.RIGHT)
ChooseType = tk.Radiobutton(TypeFrame, variable = TypeChoice, text = "只含数字的txt", font = 'Helvetica -15', value = 1).pack(side = tk.TOP)
ChooseType = tk.Radiobutton(TypeFrame, variable = TypeChoice, text = "任意txt（未实现）", font = 'Helvetica -15', value = 2).pack()
ChooseType = tk.Radiobutton(TypeFrame, variable = TypeChoice, text = "png（未实现）", font = 'Helvetica -15', value = 3).pack()
ChooseType = tk.Radiobutton(TypeFrame, variable = TypeChoice, text = "mp3（未实现）", font = 'Helvetica -15', value = 4).pack()
ChooseType = tk.Radiobutton(TypeFrame, variable = TypeChoice, text = "mp4（未实现）", font = 'Helvetica -15', value = 5).pack(side = tk.BOTTOM)

Confirm = tk.Button(OperationFrame, text = "确认", fg = "black", command = transform)
Confirm.pack(side = tk.BOTTOM)


# 右边的frame存放密钥
PasswordFrame = tk.LabelFrame(root,text = '密钥', font = 'Helvetica -15')
PasswordFrame.pack(side = tk.RIGHT)

Password = tk.Entry(PasswordFrame,font = 'Helvetica -15')
Password.pack()

root.mainloop()

'''
import tkinter
root = tkinter.Tk()
r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root,variable = r,value ='1',text='Radio1')
radio.pack()
radio = tkinter.Radiobutton(root,variable = r,value ='2',text='Radio2')
radio.pack()
radio = tkinter.Radiobutton(root,variable = r,value ='3',text='Radio3')
radio.pack()
radio = tkinter.Radiobutton(root,variable = r,value ='4',text='Radio4')
radio.pack()
c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root,
text='Checkbutton',
variable = c,
onvalue =1,
offvalue=2
)
check.pack()
root.mainloop()
print(r.get())
print(c.get())
'''