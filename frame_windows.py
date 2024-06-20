import tkinter as tk    
from tkinter import *
from tkinter import font
import tkinter.font as tkFont
from tkinter import ttk
import datetime as dt
top=tk.Tk()
top.title("BayTracker '24")
top.geometry("800x400")
top.resizable(False,False)

style = font.Font(weight='bold')

fontObj = tkFont.Font(size=36, weight='bold')
 
date = dt.datetime.now()

menu = tk.Frame(top, bg='burlywood3',padx=266,pady=77)
inventory = tk.Frame(top,bg='burlywood3')
support = tk.Frame(top, width=400,height=800,
                bg='burlywood3')

menu.grid(row=0,column=0,sticky="nsew")
inventory.grid(row=0,column=0,sticky="nsew")
support.grid(row=0,column=0,sticky="nsew")


title= Label(menu,text="BayTracker", 
             bg="burlywood3", font= fontObj)
title.pack(pady=20,padx=1)



inv = Button(menu,text="Inventory", font= style,
                command=lambda:inventory.tkraise())
inv.pack(pady=20)

spprt = Button(menu,text="Support", font = style,
               command=lambda:support.tkraise())
spprt.pack(pady=20)

time = Label(menu, text=f"{date:%B %d %Y}", font = style,
            background="burlywood3")
time.pack()
#Inventory



inv_title = Label(inventory,text="Inventory",
                  font= fontObj, bg="burlywood3")
inv_title.pack(pady=30)

tree = ttk.Treeview(inventory,column=("c1",
                    "c2"), show="headings",
                    height=7)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Name")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Quantity")

#Treeview column
tree.insert('','end', text="1", values=('tomaotoe',"2" ))

tree.pack()

inv_button = Button(inventory,text="Back", font= style,
                    command=lambda:menu.tkraise())
inv_button.pack(pady=30)


spprt_title = Label(support,text="Support",font=fontObj,
                    bg="burlywood3")
spprt_title.pack()

spprt_button = Button(support,text="Back", font= style,
                    command=lambda:menu.tkraise())
spprt_button.pack(pady=30)



menu.tkraise()
top.mainloop()