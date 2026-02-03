#Canvas
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
ca=tk.Canvas(w,bg='white') #By Default Its Invisible
ca.create_rectangle((50,20,100,200),
                    fill='cyan',
                    dash=(1,2),
                    width=10,
                    outline='lime')
#Accepts Tuples Of Format 'top left right bottom
# first dash tells how long each one should be 
# second dash tells how big the gap is
ca.create_oval((200,0,300,100),fill='yellow')
ca.create_arc((200,0,300,100),
              fill='grey',
              extent=180,
              style=tk.ARC,
              outline='purple',
              width=15)   #Going 180 Degree From The Point Where 45 Is 
ca.create_line((0,0,100,150),fill='red') #Start x,y End x,y
ca.create_polygon((0,0,100,150,300,150),fill='orange') #x1 y1 x2 y2 x3 y3......
ca.create_text((100,250),text="TEXT",fill='green')
ca.create_window((300,200),
                 window=ttk.Label(w,text="Hello"))
brush=4
ca.bind('<Motion>',draw)
ca.pack()
w.mainloop()