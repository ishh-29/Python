#Layouts
import tkinter as tk
from tkinter import ttk

#Window
w=tk.Tk()
w.geometry("400x400")
w.title("Layouts in Tkinter")

#Widgets
l1=ttk.Label(w,text="Label 1",background='red')
l2=ttk.Label(w,text="Label 2",background='blue')
#Pack
l1.pack()
l2.pack()
#Attributes Of Pack
'''
side='left'/'right'/'top'/'bottom'
expand=True/False (False By Default) Takes Available Space
fill-'x'/'y'/'both' (No Fill By Default) Fills The Available Space
'''
#Grid
w.columnconfigure(0,weight=1)
w.columnconfigure(1,weight=1)
w.columnconfigure(2,weight=2)
w.rowconfigure(0,weight=1)
w.rowconfigure(1,weight=1)
l1.grid(row=0,column=1,sticky='nsew')
l2.grid(row=1,column=1,columnspan=2,sticky='nsew')
#Place
l1.place(x=100,y=200,width=100,height=50)
l2.place(relx=0.5,rely=0.5,relwidth=0.3,relheight=0.1,anchor='center')
#Running
w.mainloop()