from tkinter import *
import tkinter.font as tkFont
from tkinter import font
from tkinter import ttk
import tkinter as tk


top = Tk()
top.title("Inventory")
top.geometry('800x400')
top.configure(background='burlywood3')

fontObj = tkFont.Font(size=36, weight='bold')
style =font.Font(weight='bold')

def back():
    top.destroy()
    import menu





inv_label = Label(top,text="Support", font=fontObj,
                  background='burlywood3')
inv_label.place(x=250, y=10)

bck_btn = Button(top,text='Back',height=1, 
                 width=10, background='burlywood2' ,command=back)
bck_btn.place(x=10,y=360)
top.mainloop()