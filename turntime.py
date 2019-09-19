# -*- coding:utf-8 -*- 

import Tkinter
import time
from Tkinter import *
import tkMessageBox as messagebox
##转换时间的小工具
window = Tk()
window.geometry("300x300+500+500")

v = IntVar()
v.set(1)
print v.set(1)
Radiobutton(window, text = "时间戳转为时间！", variable = v, value = 1 ).pack(anchor = W )
Radiobutton(window, text = "时间转为时间戳！", variable = v, value = 2 ).pack(anchor = W )

print v.get()

label= Label(window, text = u"时间搓转为时间，在下面输入时间搓");
label.pack(); # 将小部件放置到主窗口中

var = StringVar();
entry = Entry(window, textvariable = var);
entry
entry.pack();


label1 = Label(window, text = u"转换结果为：")
label1.pack()


message = Text(window, width = 40, height= 10)

def click():
	try:
		if v.get()== 1:
			t = var.get()
			st = time.localtime(float(t))
			format_time = time.strftime("%Y-%m-%d %H:%M:%S", st);
			message.insert(1.0, format_time+"\n")
		
		elif v.get() == 2:
			dt = var.get()
			format_time = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
			message.insert(2.0, str(time.mktime(format_time))+"\n")
		else:
			return
	except ValueError:
		messagebox.showerror("error", "输入正确的参数")


message.pack()

button = Button(window, text = "点击转换" ,command = click);
button.pack()


window.mainloop(); # 进入消息循环




