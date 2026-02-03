#Menus
import tkinter as tk
from tkinter import ttk
#Windows 
w=tk.Tk()
w.title("Menus")
w.geometry("600x400")
#Menu
m=tk.Menu(w)
#Sub Menu
subm=tk.Menu(m,tearoff=False) #By Default True
subm.add_command(label="New",command=lambda:print("New File"))
subm.add_command(label="Open",command=lambda:print("Open File"))
subm.add_separator()
m.add_cascade(label="Hello",menu=subm)
w.configure(menu=m)
w.mainloop()