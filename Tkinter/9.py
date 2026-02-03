#Drawing
import tkinter as tk
from tkinter import ttk
w=tk.Tk()
w.geometry('600x400')
w.title("Canvas")
#Creating Canvas
def draw(event):
    x=event.x
    y=event.y
    ca.create_oval((x-brush/2,y-brush/2,x+brush/2,y+brush/2))
def adjust(event):
    global brush
    if event.delta >0:
        brush +=4
    else :
        brush -=4
    brush=max(0,min(brush,50)) #If Size Gets Negative Max Selects Positive One
ca=tk.Canvas(w,bg='white') #By Default Its Invisible
brush=4
ca.bind('<Motion>',draw)
ca.bind('<MouseWheel>',adjust)
ca.pack()
w.mainloop()