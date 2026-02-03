#Functions And Arguements
import tkinter as tk
from tkinter import ttk
w=tk.Tk()
w.title("Functions And Arguements")
def bfunc(e_str):
    print("Button Pressed")
    print(e_str.get())
e_str=tk.StringVar(value="test")
e=ttk.Entry(w,
            textvariable=e_str)
e.pack()
#b=tk.Button(w,text="Button",command=bfunc(e_str)) Prints The Entry Attributes Without Even Pressing Button
b=tk.Button(w,text="Button",command=lambda:bfunc(e_str)) #Lambda Function Returns The Function
b.pack()
w.mainloop()