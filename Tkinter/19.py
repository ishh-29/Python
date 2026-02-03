#Scrolling
import tkinter as tk
from tkinter import ttk
from random import randint,choice

#Setting Up Window
w=tk.Tk()
w.title("Scrolling")
w.geometry('600x400')

#Creating Canvas
can=tk.Canvas(w,bg='grey',scrollregion=(0,0,2000,5000))
can.create_line(0,0,2000,5000,fill='lime',width=10)
for i in range(10):
    l=randint(0,2000)
    t=randint(0,5000)
    r=l+randint(10,500)
    b=t+randint(10,500)
    color=choice(['red','green','blue','yellow','purple','orange'])
    can.create_rectangle(l,t,r,b,fill=color)
can.pack(expand=True,fill='both')

#Mousewheel Scrolling
can.bind_all('<MouseWheel>',lambda event:can.yview_scroll(int(event.delta/120)),'units')

#Creating Scrollbar
srlbar=ttk.Scrollbar(w,orient='vertical',command=can.yview)
can.config(yscrollcommand=srlbar.set)
srlbar.place(relx=1,rely=0,relheight=1,anchor='ne')

#Running
w.mainloop()