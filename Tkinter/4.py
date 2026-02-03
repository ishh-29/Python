#Buttons
import tkinter as tk
from tkinter import ttk
w=tk.Tk()
w.title("Buttons")
w.geometry("800x1000")
#Basic Button
def press():
    print("Basic Button")
    print(radv.get())
s=tk.StringVar(value="hi")
b=ttk.Button(master=w,
             text="Button",
             command=press,
             textvariable=s
             )
b.pack()
#Check Buttons
cv=tk.Variable()
c=ttk.Checkbutton(master=w,
                  text="Check Buttons",
                  command=lambda :print(cv.get()), #We Can Set Default Value As value="True" 
                  variable=cv, #Returns 1 or 0 Which Are Of Type String Because Of StringVar
                  onvalue='True',
                  offvalue='False'
                  )#If We Set The Command Value Checkbutton Will Kinda Behave Like Radiobutton
c.pack()
#Radio Buttons
radv=tk.StringVar()
r=ttk.Radiobutton(w,
                  text="Radio Buttons",
                  value=1,
                  variable=radv,
                  command=lambda:print(radv.get()))
r.pack()
r1=ttk.Radiobutton(w,
                   text="Radio Button 1",
                   variable=radv,
                   value=0,)
r1.pack()
w.mainloop()