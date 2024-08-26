import tkinter as tk    
from tkinter import *
from tkinter import font
import tkinter.font as tkFont
from tkinter import ttk
import datetime as dt
from tkinter.messagebox import askyesno
import math
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

top=tk.Tk()
top.title("BayTracker '24")
top.geometry("800x400")
top.resizable(False,False)

style = font.Font(weight='bold')
descrip_font = tkFont.Font(family="Calibri", size= 10, weight=tkFont.NORMAL)
fontObj = tkFont.Font(size=36, weight='bold')
date = dt.datetime.now()

menu = tk.Frame(top, bg='burlywood3',padx=266,pady=77)
inventory = tk.Frame(top,bg='burlywood3')
support = tk.Frame(top,bg='burlywood3')
analytics = tk.Frame(top,bg="burlywood3")

menu.grid(row=0,column=0,sticky="nsew")
inventory.grid(row=0,column=0,sticky="nsew")
support.grid(row=0,column=0,sticky="nsew")
analytics.grid(row=0,column=0,sticky="nsew")

title= Label(menu,text="BayTracker", 
             bg="burlywood3", font= fontObj)
title.pack(pady=20,padx=1)

inv = Button(menu,text="Inventory", font= style,
                command=lambda:inventory.tkraise())
inv.pack(pady=5)

spprt = Button(menu,text="Support", font = style,
               command=lambda:support.tkraise())
spprt.pack(pady=15)

ayltics = Button(menu,text="Analytics", font=style,
                        command=lambda:analytics.tkraise())
ayltics.pack(pady=10)

exit = Button(menu,text="Exit", font = style,
             command= exit )
exit.pack()

time = Label(menu, text=f"{date:%B %d %Y}", font = style,
            background="burlywood3")
time.pack()

# Inventory
tree_view = ttk.Treeview(inventory,show="headings", height=7)

inv_title = Label(inventory,text="Inventory", font= fontObj, bg="burlywood3")
inv_title.pack(pady=5)

tree_view['columns'] = ("Name","ID",'QTY')

tree_view.column("Name", anchor=CENTER)
tree_view.column("ID", anchor=CENTER)
tree_view.column("QTY", anchor=CENTER)

tree_view.heading("Name", text="Name")
tree_view.heading("ID", text="ID")
tree_view.heading("QTY", text='QTY')

# Efficient Table
veges =[ 
['Tomato',1,'10'],
['Cucumber',2,'15'],
['Silver Beat',3,'20'],
['Chillies',4,'25'],
['Pumpkin',5,'30'],
['Beetroot',6,'35'],
['Spinach',7,'40'],
['Spring Onion',8,'45'],
['Beans',9,'50'],
['Parsnip',10,'55']
]

for records in veges:
   tree_view.insert('','end',open=True,text='',values=(records[0],records[1],records[2]))

tree_view.pack()


def edit_qty(event):
    selected_item = tree_view.selection()[0]
    column = tree_view.identify_column(event.x)
    
    if column == '#3':  
        x, y, width, height = tree_view.bbox(selected_item, column='#3')
        qty = tree_view.item(selected_item, "values")[2]

        
        entry = tk.Entry(inventory, width=10)
        entry.place(x=x, y=y + 100) 
        entry.insert(0, qty)

        # Update the QTY in Treeview and remove entry widget
        def save_qty(event):
            new_qty = entry.get()
            tree_view.item(selected_item, values=(tree_view.item(selected_item, "values")[0], tree_view.item(selected_item, "values")[1], new_qty))
            entry.destroy()
        
        # Bind Return/Enter key to save the changes
        entry.bind('<Return>', save_qty)
        entry.focus()

# Bind double-click to edit the QTY column
tree_view.bind('<Double-1>', edit_qty)




inv_button = Button(inventory,text="Back", font= style, command=lambda:menu.tkraise())
inv_button.pack(pady=5)

# Support Interface
spprt_title = Label(support,text="Support",font=fontObj, bg="burlywood3")
spprt_title.pack()

selected_vege= tk.StringVar()
vegeschosen = ttk.Combobox(support, width= 20, state="readonly", textvariable= selected_vege )

vegeschosen['values'] = (
                         'Tomato',
                         'Cucumber',
                         'Beetroot',
                         'Spinach',
                         'Beans',
                         'Chilli',
                         'Pumpkin',
                         'Parsnip',
                         'Silver Beat',
                         'Spring Onion')

vegeschosen.pack()

text = tk.Text(support,height=15, width= 50, font= descrip_font, state= NORMAL)
text.pack()

welcome = "Welcome to the support page!!!"

toma = '''Tomatoes require a warm and sunny environment.
It's period of growing season September to January.
Tomatoes also require plenty of compost and organic matter.
Every four weeks they need it for optimal growth.
Seasons - Spring and Summer.
Tomatoes harvestaion period when a bright red colour.
Aphids are the most common pest to affect tomatoes.
To get rid of them you can use Marvik Incest Pest Killer or Enspray Oil.
Their most common diseases are Bacterial Spots, Powdery Mildew and Blossom End Rot.
Bacterial Spots are tiny black spots found evenly spread on the leaves.
To prevent this happening simply remove the leaf and spray the rest of the leaves with copper spray. 
'''
ccmbr =" Cucumber"
btrt = " Beetroot"
spnch = " Spinach"
bns = " Beans"
chll = " Chilli"
pmpkn = " Pumpkin"
prsnp = " Parsnip"
slvr_bt = " Silver Beat"
sprng_nn = " Spring Onion"

def config_text():
    veg_texts = {
        "Tomato": toma,
        "Cucumber": ccmbr,
        "Beetroot": btrt,
        "Spinach": spnch,
        "Beans": bns,
        "Chilli": chll,
        "Pumpkin": pmpkn,
        "Parsnip": prsnp,
        "Silver Beat": slvr_bt,
        "Spring Onion": sprng_nn}

    selected = selected_vege.get()
    if selected in veg_texts:
        text.config(state=NORMAL)
        text.delete(1.0, END)
        text.insert(INSERT, veg_texts[selected])
        text.config(state=DISABLED)

apply = Button(support,text='Apply', font= style, command=config_text)
apply.pack() 

def refresh():
    menu.tkraise()
    support.destroy()
    support.__init__()

spprt_button = Button(support,text="Back", font= style, command=refresh)
spprt_button.pack(pady=5)

# Analytics
ayltics_title = Label(analytics,text="Analytics", font= fontObj, bg="burlywood3")
ayltics_title.pack()

def plot():
    fig = Figure(figsize =(3,3), dpi=100)
    y = [i*2 for i in range(100)]
    
    plot1= fig.add_subplot(111)
    plot1.plot(y)

    Canvas= FigureCanvasTkAgg(fig, master=analytics)
    Canvas.draw()

    Canvas.get_tk_widget().pack()

    toolbar= NavigationToolbar2Tk(Canvas, analytics)
    toolbar.update()

    Canvas.get_tk_widget().pack()

plot()

ayltcs_button = Button(analytics,text="Back",font=style, command=lambda:menu.tkraise())
ayltcs_button.pack()  

text.insert(tk.END,welcome)
menu.tkraise()
top.mainloop()
