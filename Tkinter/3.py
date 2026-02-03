#Tkinter Variables
import tkinter as tk
from tkinter import ttk
def press():
    print(st.get())
    st.set("Button Pressed")
w=tk.Tk()
w.title("Tkinter Variables")
st=tk.StringVar() #We Can Assign Start Value As value="start"
l=ttk.Label(master=w,text="Label",textvariable=st)
l.pack()
e=ttk.Entry(master=w,text="Entry",textvariable=st)
e.pack()
e1=ttk.Entry(master=w,text="Entry1",textvariable=st)
e1.pack()
#This Is Because They All Share Same Variable
b=ttk.Button(master=w,text="Entry",command=press)
b.pack()
w.mainloop()
