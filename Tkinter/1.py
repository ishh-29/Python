#Miles To Kilometer Converter
import tkinter as tk
#from tkinter import ttk
#Since Tkinter Styling Is Limited,There's External Module
import ttkbootstrap as ttk
def convert():
    #print(entry.get()) <- This Is Usually Not Used Cause Of Efficiency
    #print(e_int.get())
    miles=e_int.get()
    km=miles*1.6
    #for example 
    ol_str.set(km)

#Creating Window 
w=ttk.Window(themename="journal")
#w=tk.Tk()
w.title("Ishan's Page") #<-Changes The Name Of Gui
w.geometry("300x150") #WidthxHeight
#Creating Widget
l=ttk.Label(master=w,
            text="Miles To Kilometer Converter",
            font="ComicSansMS 14") #Fontname Font Size
l.pack()
#You Can Add Bold,Italic And Underline Too
#Creating Feilds
f=ttk.Frame(master=w)
e_int=tk.IntVar() #<- Stores And Updates The Values
entry=ttk.Entry(master=f,
                textvariable=e_int) 
#Here Master Is Frame #Everything Entered In Entry Will Be Stored In e_int
button=ttk.Button(master=f,
                  text="Convert ",
                  command=convert)
entry.pack(side="right",padx=10)
button.pack(side="right")
f.pack(pady=10)
#Output Feilds
ol_str=tk.StringVar()
ol=ttk.Label(master=w,text="",
             font="ComicSansMS 10",
             textvariable=ol_str)
#Text Variable Overwrites Whatever Text In The Label,Used To Update The Lable Dynamically
ol.pack(pady=5)
w.mainloop() #Updates The Gui;Checks For Events;Runs Until It Is Closed