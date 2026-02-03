#Frames And Parenting
import tkinter as tk
from tkinter import ttk
w=tk.Tk()
w.geometry('600x400')
w.title("Frames And Parenting")
#Frame
f=ttk.Frame(w,
            width=100,
            height=200,
            borderwidth=10,
            relief='groove') #sunken,raised,flat,ridge
f.pack() #side-> default 'top'
#Parenting/Master Setting
l=ttk.Label(f,text="Label In Frame") #Ttk Sets The Size Of Parents By Their Children 
#To Disable This,Use pack_propagate(True/False)
l.pack()
w.mainloop()