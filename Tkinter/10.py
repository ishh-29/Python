#Treeview
import tkinter as tk
from tkinter import ttk
from random import choice
w=tk.Tk()
w.geometry('600x400')
w.title("Treeview")
fname=['a','b','c','d','e','f','g','h','i','j','k']
age=[2,11,13,22,18,16,55,76,45,32,10]
def select(_):
    print(t.selection())
    for i in t.selection():
        print(t.item(i)['values'])
def delt(_):
    for i in t.selection():
        t.delete(i)
#Creating Treeview
t=ttk.Treeview(w,
               columns=("name","age"),
               show='headings')
t.heading("name",text="Names")
t.heading("age",text="Age")
#Inserting Values In The Table
for i in range(100):
    n=choice(fname)
    l=choice(age)
    r=(n,l)
    t.insert(parent="",index=0,values=(r)) #Usually An Empty String
#Table Events
t.bind('<<TreeviewSelect>>',select)
#t.bind('<<TreeviewSelect>>',lambda event : print(t.selection())) #Gives Random Number
t.bind('<Delete>', delt)
t.pack(fill='both',expand=True)
w.mainloop()