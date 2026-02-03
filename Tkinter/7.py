#Combobox And Spinbox 
import tkinter as tk 
from tkinter import ttk 
w=tk.Tk()
w.title('Combobox And Spinbox')
w.geometry("600x400")
#Combobox
items=[1,2,3,4,5,6,7]
f_str=tk.StringVar(value=items[4])
co=ttk.Combobox(w,textvariable=f_str)
co['values']=items
co.bind('<<ComboboxSelected>>',
        lambda event :co_label.config(text=f'Selected Item :({f_str.get()})'))
co.pack()
co_label=ttk.Label(w,text="A Label")
co_label.pack()
#Spinbox
s_int=tk.IntVar(value=3)
s=ttk.Spinbox(w,
              from_=3,
              to=20,
              increment=1,
              command=lambda:print(s_int.get()),
              textvariable=s_int)
#s['value']=(1,2,3,4,5,6,7,8,9,10)
s.bind('<<Increment>>',lambda event : print("up"))
s.bind('<<Decrement>>',lambda event : print("down"))
s.pack()
w.mainloop()