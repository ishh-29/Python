#Responsive Layout

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self,start_size):
        super().__init__()
        self.title("Responsive Layout")
        self.geometry(f'{start_size[0]}x{start_size[1]}')
        self.frame=ttk.Frame(self)  
        self.frame.pack(expand=True,fill='both')              
        SizeNotifier(self,{600:self.create_medium,
                           300:self.create_small,
                           1200:self.create_large
                           })
        self.mainloop()

    def create_small(self):
        self.frame.pack_forget()
        self.frame=ttk.Frame(self)
        ttk.Label(self.frame,text="Label 1",background='red').pack(expand=True,fill='both',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 2",background='green').pack(expand=True,fill='both',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 3",background='blue').pack(expand=True,fill='both',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 4",background='yellow').pack(expand=True,fill='both',padx=10,pady=5)
        self.frame.pack(expand=True,fill='both')

    def create_medium(self):
        self.frame.pack_forget()
        self.frame=ttk.Frame(self)
        self.frame.columnconfigure((0,1),weight=1,uniform='a')
        self.frame.rowconfigure((0,1),weight=1,uniform='a')
        self.frame.pack(expand=True,fill='both')
        ttk.Label(self.frame,text="Label 1",background='red').grid(row=0,column=0,sticky='nsew',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 2",background='green').grid(row=0,column=1,sticky='nsew',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 3",background='blue').grid(row=1,column=0,sticky='nsew',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 4",background='yellow').grid(row=1,column=1,sticky='nsew',padx=10,pady=5)

    def create_large(self):
        self.frame.pack_forget()
        self.frame=ttk.Frame(self)
        self.frame.columnconfigure((0,1,2),weight=1,uniform='a')
        self.frame.rowconfigure((0,1),weight=1,uniform='a')
        self.frame.pack(expand=True,fill='both')
        ttk.Label(self.frame,text="Label 1",background='red').grid(row=0,column=0,sticky='nsew',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 2",background='green').grid(row=0,column=1,sticky='nsew',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 3",background='blue').grid(row=0,column=2,sticky='nsew',padx=10,pady=5)
        ttk.Label(self.frame,text="Label 4",background='yellow').grid(row=1,column=0,sticky='nsew',padx=10,pady=5)
        
class SizeNotifier:

    def __init__(self,w,size_dict):
        self.w=w
        self.size_dict={i:j for i,j in sorted(size_dict.items())}
        self.curr_minsize=None
        self.w.bind('<Configure>',self.check_size)
        self.w.update()
        minheight=self.w.winfo_height()
        minwidth=list(self.size_dict)[0]
        self.w.minsize(minwidth,minheight)
        print(self.size_dict)

    def check_size(self,event):
        if event.widget==self.w:
            w_width=event.width
            checked_size=None
            for i in self.size_dict:
                delta=w_width - i
                if delta>=0:
                    checked_size=i
            if checked_size !=self.curr_minsize:
                self.curr_minsize=checked_size
                self.size_dict[self.curr_minsize]()

app=App((400,600))