#Windows And Widgets
import tkinter as tk
from tkinter import ttk
def press():
    e1=e.get()
    l.config(text=e1)
    e['state']='disabled' #Enabling Or Disabling The Widget From Working
    #For Viewing 'what you can do with a widget :
    print(l.configure())
def text():
    print(e.get())
    #For Updating Widget 
    l.config(text="Test 1")
    #Other Method -> l[old]=new
#Creating A Window
w=tk.Tk()
w.title("Window And Widgets")
w.geometry('800x500')
#Creating Widgets(tk)
tk.Text(master=w).pack() #<-Multiline Text Input
#Creating Widgets(ttk)
l=ttk.Label(master=w,text="Test") 
l.pack() 
#Placed Below Text Because Created It Is After 
e=ttk.Entry()
e.pack()
l1=ttk.Label(master=w,text="My Label")
l1.pack()
b=ttk.Button(master=w,text="Button",command=press)
b.pack()
b1=ttk.Button(master=w,text="Button 1",command=text)
b1.pack()
w.mainloop()