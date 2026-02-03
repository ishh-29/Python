import tkinter as tk 
from tkinter import ttk
#Functional Approach
def create_segment(parent,label,button):
    frame=ttk.Frame(master=parent)
    #Creating Grid Layout
    frame.rowconfigure(0,weight=1)
    frame.columnconfigure((0,1,2),weight=1,uniform="a")
    #Creating Components
    ttk.Label(frame,text=label).grid(row=0,column=0,sticky='nsew')
    ttk.Button(frame,text=button).grid(row=0,column=1,sticky='nsew')
    return frame

class Segment(ttk.Frame):
    def __init__(self,parent,label,button):
        super().__init__(master=parent)
        #Creating Grid Layout
        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1,2),weight=1,uniform="a")
        #Creating Components
        ttk.Label(self,text=label).grid(row=0,column=0,sticky='nsew')
        ttk.Button(self,text=button).grid(row=0,column=1,sticky='nsew')
        #Placing The Componets
        self.pack(expand=True,fill='both',padx=10,pady=10)

#Window
w=tk.Tk()
w.title("Widgets With Classes")
w.geometry("400x600")

#Widgets
Segment(w,"Label1","Button1")
Segment(w,"Label2","Button2")
Segment(w,"Label3","Button3")
#create_segment(w,"Label","Button").pack(expand=True,fill='both',padx=10,pady=10)
#Running
w.mainloop()