#Do not make any changes in this code snippet, apart from resizing the UI image as instructed in the lines below
#Before you begin, import "Pillow" (version 9.3.0) package using your in-IDE package installer or through terminal using "pip install Pillow=9.3.0"

import tkinter as Tk
import tkinter
from tkinter import *
from tkinter import ttk
import time
from PIL import Image, ImageTk

gui = Tk()
gui.geometry('1250x1080')
gui.config(bg="grey")
gui.title('Planner X - Developer 1.0.1') #add title

canvas4 = Canvas(gui, width=1535, height=1100, bg="Black", bd=0, highlightthickness=0) # Resize this and the LINE 19 equally, so as to fit the UI on your entire screen
gui.state('zoomed')
start_time5 = time.time()
canvas4.pack()

img4= Image.open(r'Rocket.png') # Replace this path with the vehicle's image that you have been assigned for
img4= img4.resize((1535,800))
img4 = ImageTk.PhotoImage(img4)

chng2 = canvas4.create_image(0,0, anchor=NW, image=img4)
chng3 = canvas4.create_text(1280, 55, text="Rocket",font=("Arial", 25),fill='red')

slave_devices = ["a", "b", "c"] # these are just dummy list components, do not worry about them


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Motor Y", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=845, y=480)

textbox1 = Entry(canvas4, width=5)  
textbox1.place(x=845, y=510)
textbox1.insert(0, "LL")

def delete_text(event):
    if textbox1.get()=="LL":
        textbox1.delete(0, tkinter.END)

textbox1.bind("<FocusIn>", delete_text)

textbox2 = Entry(canvas4, width=5)  
textbox2.place(x=885, y=510)
textbox2.insert(0, "UL")

def delete_text(event):
    if textbox2.get()=="UL":
        textbox2.delete(0, tkinter.END)

textbox2.bind("<FocusIn>", delete_text)


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Motor X", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=720, y=480)

textbox3 = Entry(canvas4, width=5)  
textbox3.place(x=720, y=510)
textbox3.insert(0, "LL")

def delete_text(event):
    if textbox3.get()=="LL":
        textbox3.delete(0, tkinter.END)

textbox3.bind("<FocusIn>", delete_text)

textbox4 = Entry(canvas4, width=5)  
textbox4.place(x=760, y=510)
textbox4.insert(0, "UL")

def delete_text(event):
    if textbox4.get()=="UL":
        textbox4.delete(0, tkinter.END)

textbox4.bind("<FocusIn>", delete_text)


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Fin 3", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=425, y=440)

textbox5 = Entry(canvas4, width=5)  
textbox5.place(x=425, y=470)
textbox5.insert(0, "LL")

def delete_text(event):
    if textbox5.get()=="LL":
        textbox5.delete(0, tkinter.END)

textbox5.bind("<FocusIn>", delete_text)

textbox6 = Entry(canvas4, width=5)  
textbox6.place(x=465, y=470)
textbox6.insert(0, "UL")

def delete_text(event):
    if textbox6.get()=="UL":
        textbox6.delete(0, tkinter.END)

textbox6.bind("<FocusIn>", delete_text)


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Fin 1", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=390, y=300)

textbox7 = Entry(canvas4, width=5)  
textbox7.place(x=390, y=330)
textbox7.insert(0, "LL")

def delete_text(event):
    if textbox7.get()=="LL":
        textbox7.delete(0, tkinter.END)

textbox7.bind("<FocusIn>", delete_text)

textbox8 = Entry(canvas4, width=5)  
textbox8.place(x=430, y=330)
textbox8.insert(0, "UL")

def delete_text(event):
    if textbox8.get()=="UL":
        textbox8.delete(0, tkinter.END)

textbox8.bind("<FocusIn>", delete_text)


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Fin 2", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=270, y=500)

textbox9 = Entry(canvas4, width=5)  
textbox9.place(x=270, y=530)
textbox9.insert(0, "LL")

def delete_text(event):
    if textbox9.get()=="LL":
        textbox9.delete(0, tkinter.END)

textbox9.bind("<FocusIn>", delete_text)

textbox10 = Entry(canvas4, width=5)  
textbox10.place(x=310, y=530)
textbox10.insert(0, "UL")

def delete_text(event):
    if textbox10.get()=="UL":
        textbox10.delete(0, tkinter.END)

textbox10.bind("<FocusIn>", delete_text)


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Fin 4", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=230, y=350)

textbox12 = Entry(canvas4, width=5)  
textbox12.place(x=230, y=380)
textbox12.insert(0, "LL")

def delete_text(event):
    if textbox12.get()=="LL":
        textbox12.delete(0, tkinter.END)

textbox12.bind("<FocusIn>", delete_text)

textbox11 = Entry(canvas4, width=5)  
textbox11.place(x=270, y=380)
textbox11.insert(0, "UL")

def delete_text(event):
    if textbox11.get()=="UL":
        textbox11.delete(0, tkinter.END)

textbox11.bind("<FocusIn>", delete_text)


node_map2_val = StringVar()
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, "Ejection", *slave_devices)
node_map2.config(width=7)
node_map2.place(x=1335, y=400)

textbox13 = Entry(canvas4, width=5)  
textbox13.place(x=1335, y=430)
textbox13.insert(0, "LL")

def delete_text(event):
    if textbox13.get()=="LL":
        textbox13.delete(0, tkinter.END)

textbox13.bind("<FocusIn>", delete_text)

textbox14 = Entry(canvas4, width=5)  
textbox14.place(x=1375, y=430)
textbox14.insert(0, "UL")

def delete_text(event):
    if textbox14.get()=="UL":
        textbox14.delete(0, tkinter.END)

textbox14.bind("<FocusIn>", delete_text)


gui.mainloop()
