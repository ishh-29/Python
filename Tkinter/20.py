#Scrollable Widgets
import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):

    def __init__(self,parent,text,item_h):
        super().__init__(master=parent)
        self.pack(expand=True,fill='both')
        #Widget Data
        self.text=text
        self.itemnum=len(text)
        self.height=self.itemnum*item_h
        #Canvas
        self.canvas=tk.Canvas(self,bg='lightgrey',scrollregion=(0,0,self.winfo_width(),self.height))
        self.canvas.pack(expand=True,fill='both')
        #Widget Frame / Display 
        self.frame=ttk.Frame(self)
        for i,j in enumerate(self.text):
            self.create_item(i,j).pack(expand=True,fill='x',padx=4,pady=10)
        self.canvas.create_window((0,0),window=self.frame,
                                  anchor='nw',width=self.winfo_width(),height=self.height)
        #Events
        self.canvas.bind_all('<MouseWheel>',lambda event:self.canvas.yview_scroll(int(event.delta/120),'units'))
        self.bind('<Configure>',self.update_size)
    
    def update_size(self,event):
        if self.height>=self.winfo_height():
            height=self.height
            self.canvas.bind_all('<MouseWheel>',lambda event:self.canvas.yview_scroll(int(event.delta/120),'units'))

        else:
            height=self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')

        self.canvas.create_window((0,0),window=self.frame,
                                  anchor='nw',width=self.winfo_width(),height=self.height)
    
    def create_item(self,index,item):
        frame=ttk.Frame(self.frame)
        #Creating Grid Layout
        frame.rowconfigure(0,weight=1)
        frame.columnconfigure((0,1,2,3,4),weight=1,uniform='a')
        #Creating Widgets
        ttk.Label(frame,text=f'#{index}').grid(row=0,column=0)
        ttk.Label(frame,text=f'#{item[0]}').grid(row=0,column=1)
        ttk.Button(frame,text=f'{item[1]}').grid(row=0,column=2,columnspan=3,sticky='nsew')
        return frame
#Setting Up Window
w=tk.Tk()
w.title("Scrolling")
w.geometry('600x400')
text=[('label1','button1'),('label2','button2'),('label3','button3'),
      ('label4','button4'),('label5','button5'),('label6','button6')]
list_frame=ListFrame(w,text,100)
#Running
w.mainloop()