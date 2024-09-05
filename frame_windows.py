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

descrip_font = tkFont.Font(family="Calibri", size=10,
                           weight=tkFont.NORMAL)

fontObj = tkFont.Font(size=36, weight='bold')
 
date = dt.datetime.now()

#Frames/Interfaces
menu = tk.Frame(top, bg='burlywood3', padx=266, pady=77)
inventory = tk.Frame(top, bg='burlywood3')
support = tk.Frame(top, bg='burlywood3')
analytics = tk.Frame(top, bg="burlywood3")

menu.grid(row=0, column=0, sticky="nsew")
inventory.grid(row=0, column=0, sticky="nsew")
support.grid(row=0, column=0, sticky="nsew")
analytics.grid(row=0, column=0, sticky="nsew")

#Menu Frame/Interface
title= Label(menu, text="BayTracker", 
             bg="burlywood3", font=fontObj)
title.pack(pady=20,padx=1)

#Menu Buttons
inv = Button(menu, text="Inventory", font=style,
                command=lambda:inventory.tkraise())
inv.pack(pady=5)

spprt = Button(menu, text="Support", font=style,
               command=lambda:support.tkraise())
spprt.pack(pady=15)

ayltics = Button(menu, text="Analytics", font=style,
                        command=lambda:analytics.tkraise())
ayltics.pack(pady=10)

time = Label(menu, text=f"{date:%B %d %Y}", font=style,
            background="burlywood3")
time.pack()
#Inventory Frame/Interface

tree_view = ttk.Treeview(inventory, show="headings",
                    height=7)



inv_title = Label(inventory, text="Inventory",
                  font=fontObj, bg="burlywood3")
inv_title.pack(pady=5)

tree_view['columns'] = ("Name", "ID", 'QTY')

tree_view.column("Name", anchor=CENTER)
tree_view.column("ID", anchor=CENTER)
tree_view.column("QTY", anchor=CENTER)

tree_view.heading("Name", text="Name")
tree_view.heading("ID", text="ID")
tree_view.heading("QTY", text='QTY')

#Multi-Dimensional List
veges = [ 
['Tomato',1,''],
['Cucumber',2,''],
['Silver Beat',3,''],
['Chillies',4,''],
['Pumpkin',5,''],
['Beetroot',6,''],
['Spinach',7,''],
['Spring Onion',8,''],
['Beans',9,''],
['Parsnip',10,'']
]

for records in veges:
   tree_view.insert('','end', open=True, text='',
                    values = (records[0], records[1],
                    records[2]))

tree_view.pack()

#Edit Quantity
def edit_qty(event):
    selected_item = tree_view.selection()[0]
    column = tree_view.identify_column(event.x)
    
    if column == '#3':  
        x, y, width, height = tree_view.bbox(selected_item, column='#3')
        qty = tree_view.item(selected_item, "values")[2]

        
        entry = tk.Entry(inventory, width=10)
        entry.place(x=x, y=y + 100) 
        entry.insert(0, qty)

        
        def save_qty():
            new_qty = entry.get()
            tree_view.item(selected_item, values=(tree_view.item(selected_item, "values")[0],
                                                  tree_view.item(selected_item, "values")[1], new_qty))
            entry.destroy()
        
        
        entry.bind('<Return>', save_qty)
        entry.focus()


tree_view.bind('<Double-1>', edit_qty)


inv_button = Button(inventory, text="Back", font=style,
                    command=lambda:menu.tkraise())
inv_button.pack(pady=5)

#Support Frame/Interface

spprt_title = Label(support, text="Support", font=fontObj,
                    bg="burlywood3")
spprt_title.pack()

selected_vege= tk.StringVar()

#Vegetable Selection
vegeschosen = ttk.Combobox(support, width=20,
                           state="readonly",
                            textvariable=selected_vege )
#Vegetable Options
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

#Text Widget frame 
text = tk.Text(support, height=15, width=50,
               font=descrip_font, state=NORMAL)
text.pack()

#Text Varibles
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
ccmbr ='''Cucumbers are grown on wooden stakes or trellis.
They require full sun and are planted with organic matter for optimal growth.
The period that you can grow Cucumbers are September to January, Spring - Summer.
Cucumbers are mature when they are mostly long and dark green."
'''
btrt = ''' Beetroots are grown in pots or garden beds.
They require full sun and can take up to 3 - 4 months till you're able to harvest. Beetroots require 20 cm depth of soil.
The period that you can grow beetroots are July - April, Winter - Autumn."
'''
spnch = ''' Spinach needs full sun to part shade. Requires compost for growth.
The period that you can grow spinach, February - November, Summer - Spring.
Spinach is to be harvested a mature leaf at a time as it continues to grow"
'''
bns = ''' Beans require full sun and space plus long support poles, the period of growing season is October to February.
Seasons - Spring and Summer. Beans are to be harvested after 50-60 days.
'''

chll = '''Chillies require heat and the sun to grow efficiently.
Period that you can grow chillies, September - December, Spring -Summer.
They take 3 months to mature and harvest. 
'''

pmpkn = ''' Pumpkins require a sunny position.
The period that you can grow pumpkins, September - December. They take 4-6 months to mature and require a lot of space. Spring -Summer.
'''

prsnp = ''' Parsnips are to be grown with fertile soil.
They require full sun and are harvested in at least 18 weeks.
The period to grow parsnips are July - December, Winter - Summer.
'''

slvr_bt = '''Silver Beats are grown all year round.
Their harvesting period is 8-12 weeks while being able to produce all year round.
They require full sun and fertiliser every 4 weeks for optimal growth.
'''

sprng_nn = '''Spring Onion needs to be positioned in  full sun, and requires fertiliser and leafy greens for optimal growth.
The period that you can grow Spring Onions, October - March, Spring - Summer. Springs Onions take a couple of months to mature
and can be harvested in Spring or late summer
'''


#Configuration of Text Widget
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

#Config
apply = Button(support, text='Apply', font=style,
               command=config_text)
apply.pack() 

spprt_button = Button(support, text="Back", font=style,
                      command=lambda:menu.tkraise())
spprt_button.pack(pady=5)

#Analytics Frame/Interface

ayltics_title = Label(analytics, text="Analytics",
                  font= fontObj, bg="burlywood3")
ayltics_title.pack()

#Graph
def plot():
    fig = Figure(figsize =(3,3),
                 dpi=100)
    y = [i*2 for i in range(100)]
    
    plot1= fig.add_subplot(111)

    plot1.plot(y)

    Canvas= FigureCanvasTkAgg(fig,
                              master=analytics)
    Canvas.draw()

    Canvas.get_tk_widget().pack()

    toolbar= NavigationToolbar2Tk(Canvas,
                                  analytics)
    toolbar.update()

    Canvas.get_tk_widget().pack()

plot()

ayltcs_button = Button(analytics, text="Back", font=style,
                       command=lambda:menu.tkraise())
ayltcs_button.pack()  


text.insert(tk.END,welcome)
menu.tkraise()
top.mainloop()
