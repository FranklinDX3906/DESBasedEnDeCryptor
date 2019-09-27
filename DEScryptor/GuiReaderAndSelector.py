#coding:UTF-8

import tkinter as tk
from future.moves.tkinter import filedialog
from tkinter import Variable
import CryptorOfNumberFile as c

def open_file():#打开文件，读取路径
    filepath = filedialog.askopenfilename()
    file = open(filepath)
    filecontent = file.read()
    FilePath.set(filepath)
    FileContent.set(filecontent)
    ShowPath.set(filepath)

def transform():
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

ShowPath = tk.StringVar()#展示选择文件的目录
ShowPath.set("")
ShowPathLabel = tk.Label(FileFrame, textvariable = ShowPath, font = 'Helvetica -15')
ShowPathLabel.pack()

FilePath = tk.StringVar()#选择文件的按钮
FileContent = tk.StringVar()
OpenFile = tk.Button(FileFrame, text = "选择文件",fg = "black", command = open_file)
OpenFile.pack(side = tk.BOTTOM)

#右边的frame存放选择
ChooseFrame = tk.LabelFrame(root, text = "选择你要执行的操作",font = 'Helvetica -15')
ChooseFrame.pack(side = tk.RIGHT)

OperationChoice = tk.IntVar()#选项类别
ChooseOperation = tk.Radiobutton(ChooseFrame, variable = OperationChoice, text = "加密", font = 'Helvetica -15', value = 1).pack(side = tk.TOP)
ChooseOperation = tk.Radiobutton(ChooseFrame, variable = OperationChoice, text = "解密", font = 'Helvetica -15', value = 2).pack()

Confirm = tk.Button(ChooseFrame, text = "确认", fg = "black", command = transform)
Confirm.pack(side = tk.BOTTOM)

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