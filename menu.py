import tkinter as tk    
from tkinter import *
import datetime as dt
from tkinter import font
import tkinter.font as tkFont


#Aesthetics
top=tk.Tk()
top.title("BayTracker '24")
top.geometry("800x400")
top.configure(background="burlywood3")

date = dt.datetime.now()

style =font.Font(weight='bold')

fontObj = tkFont.Font(size=36, weight='bold')



def inv_menu():
    top.destroy()
    import inv_window





def spprt_menu():
    top.destroy()
    import spprt_window



# Menu 

title= Label(top,text="BayTracker", 
             bg="burlywood3",
             font = fontObj)
title.place(x=250, y=10) 

b1 = Button(top, text ='Inventory',
            font= style,
            command= inv_menu)
b1.place(x=350,y=250)

b2 = Button(top, text ='Support',
            font= style,
            command=spprt_menu)
b2.place(x=350,y=300)

b3 = Button(top,text ='Analysis',
            font= style)
b3.place(x=350,y=350) 

  #Real-Time
time = Label(top, text=f"{date:%B %d %Y}", font = style,
            background="burlywood3")
time.place(x=600, y= 50)






top.mainloop()