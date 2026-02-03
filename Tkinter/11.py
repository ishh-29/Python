#Scales And Sliders
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
w=tk.Tk()
w.geometry('600x400')
w.title("Scales And Sliders")
#Creating Slider
sl_int=tk.IntVar(value=3)
sl=ttk.Scale(w,
              command=lambda value : print(value) ,    #pb.stop()
              from_=0,
              to=100,
              length=300,
              orient='vertical',  #Default Is Horizontal
              variable=sl_int,
              )
sl.pack()
#CreatingProgress Bar
pb=ttk.Progressbar(w,
                   variable=sl_int,
                   orient='horizontal',
                   mode='indeterminate',
                   length=250)
#pb.start(1000) #Time For Moving The Bar (In Millisecond)
pb.pack()
#Creating Scrolled Text
scrlt=scrolledtext.ScrolledText(w,width=200,height=20)
scrlt.pack()
w.mainloop()