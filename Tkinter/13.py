#Tabs
import tkinter as tk 
from tkinter import ttk 
#Window 
w=tk.Tk()
w.geometry('600x400')
w.title("Tabs")
nb=ttk.Notebook(w)
#Tab 1
t1=ttk.Frame(nb)
l1=ttk.Label(t1,text="Enter Text")
l1.pack()
b1=ttk.Button(t1,text="Button 1")
b1.pack()
#Tab 2
t2=ttk.Frame(nb)
l2=ttk.Label(t2,text="Enter Text")
l2.pack()
b2=ttk.Button(t2,text="Button 2")
b2.pack()
nb.add(t1,text="Tab1")
nb.add(t2,text="Tab2")
nb.pack()
w.mainloop()