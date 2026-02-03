#Customizing The Window
import tkinter as tk
from tkinter import ttk
#Window
w=tk.Tk()
w.title("Customizing The Window")
w.geometry("600x400")
w.iconbitmap("favicon.ico") #For Changing The Icon

#Setting Up Size Constraints
w.minsize(300,200) #Minimum Size Of The Window
w.maxsize(800,600) #Maximum Size Of The Window
#w.resizable(True, False) Width Resizable, Height Not Resizable
#To Get Width And Height Of The Screen
print(w.winfo_screenwidth(),w.winfo_screenheight())
#Window Attributes
'''
w.attributes("-alpha",0.5) To Set The Transparency Of The Window
w.attributes("-topmost",True) To Keep The Window On Top
'''

#Setting Up Security Event
w.bind('<Escape>',lambda event:w.quit()) #To Close The Window On Pressing Escape Key

'''
Some Attributes Make The Window Impossible To Close
w.attributes("-disabled",True) #To Disable The Window
w.atributes("fullscreen",True) #To Make The Window Fullscreen
It Is Going To Raise Error Due To Max Window Size
'''
#Modifying Title Bar
w.overrideredirect(True) #To Remove The Title Bar
grip=ttk.Sizegrip(w)
grip.place(relx=1.0,rely=1.0,anchor='se')

#Running
w.mainloop()