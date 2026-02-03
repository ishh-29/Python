#Event Binding
import tkinter as tk 
from tkinter import ttk
w=tk.Tk()
w.geometry("600x500")
w.title("Event Binding")
def pos(event):
    print(f"x : {event.x} y : {event.y}")
t=tk.Text(w)
t.pack()
e=ttk.Entry(w)
e.pack()
b=ttk.Button(w,text="A Button")
b.pack()
#Events
#w.bind('<Alt-Key-a>',lambda event : print("An Event")) #event -> '<modifier-type-detail>'
b.bind('<Alt-KeyPress-a>',lambda event : print(event))
w.bind('<Motion>', pos) 
w.bind('<KeyPress>', lambda event : print(f'Button Pressed Was ({event.char})')) 
#Prints-> <KeyPress event
#send_event=True state=0x20000
#keysym=a keycode=65 char='a' x=205 y=223> {x and y are position of the widget}
w.mainloop()