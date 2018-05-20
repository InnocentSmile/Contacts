from tkinter import *
from tkinter import messagebox

from 通讯录Mysql.people import people
from 通讯录Mysql.peopledao import Peopledao


class adresslist:
    def __init__(self):
        self.Index = 0
        self.dao = Peopledao()
        self.ret = self.dao.findall()
        # print(self.ret)
        self.winone()


    def winone(self):
        windows=Tk()
        windows.title("通讯录Mysql")
        self.nameEntry1=StringVar()
        self.nameEntry1.set("请输入姓名查找号码")
        #第一行
        Entry(textvariable=self.nameEntry1).grid(row=1,column=2)
        Button(text="查找",width=10,command=self.search).grid(row=1,column=3)
        # 第二行
        self.nameEntry = StringVar()
        Label(text="姓名:").grid(row=2,column=1)
        Entry(textvariable=self.nameEntry).grid(row=2, column=2)
        # 第三行
        self.TelEntry = StringVar()
        Label(text="Tel:").grid(row=3, column=1)
        Entry(textvariable=self.TelEntry).grid(row=3, column=2)
        # 第四行
        Button(text=">>",width=15,command=self.loadNext).grid(row=4, column=3)
        Button(text="<<",width=15,command=self.loadPrev).grid(row=4, column=2)
        # 第五行
        Button(text="添加",width=10,command=self.addpeople).grid(row=5, column=1)
        Button(text="修改",width=10,command=self.updatepeople).grid(row=5, column=2)
        Button(text="删除",width=10,command=self.deletepeople).grid(row=5, column=3)
        # # 第六行
        # Label(text="显示反馈信息").grid(row=6, column=1)

        if self.ret==():
            self.nameEntry.set("")
            self.TelEntry.set("")
        else:
            self.show(self.ret[self.Index])

        windows.mainloop()
    #对传入的元组分解赋值
    def show(self,pTuple):
        self.nameEntry.set(pTuple[1])
        self.TelEntry.set(pTuple[2])
    #按条件查询显示结果
    def search(self):
        searchname=self.nameEntry1.get()
        result=self.dao.find(searchname)

        for i in range(len(self.ret)):
            if self.ret[i]==result[0]:
                self.Index=i
        # print(result)
        self.show(self.ret[self.Index])
    #下一个
    def loadNext(self):
        if self.Index < len(self.ret)-1:
            self.Index+=1
            self.show(self.ret[self.Index])
        else:
            messagebox.showinfo("提示信息", "已经是最后一个了")
            # print(self.Index)
    # 上一个
    def loadPrev(self):
        if self.Index > 0:
            self.Index-=1
            self.show(self.ret[self.Index])
        else:
            messagebox.showinfo("提示信息", "已经是第一个了")
            # print(self.Index)


    def addpeople(self):
        try:
            name=self.nameEntry.get()
            tel=self.TelEntry.get()
            p=people(name,tel)
            self.dao.addpeople(p)
            messagebox.showinfo("提示信息", "添加成功")
            self.ret = self.dao.findall()
            self.Index=len(self.ret)-1
            self.show(self.ret[self.Index])

        except:
            messagebox.showinfo("提示信息", "添加失败")

    def updatepeople(self):
        try:
            name=self.nameEntry.get()
            tel=self.TelEntry.get()
            p=people(name,tel)
            self.dao.myupdate(p)
            messagebox.showinfo("提示信息", "修改成功")
            self.ret = self.dao.findall()
            self.show(self.ret[self.Index])
        except:
            messagebox.showinfo("提示信息", "修改失败")

    def deletepeople(self):
        try:
            name = self.nameEntry.get()
            tel = self.TelEntry.get()
            p = people(name, tel)
            self.dao.mydelete(p)

            self.ret = self.dao.findall()
            messagebox.showinfo("提示信息", "删除成功")


            if self.ret == ():
                self.nameEntry.set("")
                self.TelEntry.set("")
            else:
                self.Index = 0
                self.show(self.ret[self.Index])




        except:
            messagebox.showinfo("提示信息", "删除失败")


if __name__ == '__main__':
    adresslist()



































