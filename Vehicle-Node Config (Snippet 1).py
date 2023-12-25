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
gui.title('Planner X - Developer 1.0.1')

canvas4 = Canvas(gui, width=1535, height=1100, bg="Black", bd=0, highlightthickness=0) # Resize this and the LINE 19 equally, so as to fit the UI on your entire screen
gui.state('zoomed')
start_time5 = time.time()
canvas4.pack()

img4= Image.open(r'C:\Users\User\Desktop\AUTO PILOT\Mapping\Satellite.png') # Replace this path with the vehicle's image that you have been assigned for
img4= img4.resize((1535,800))
img4 = ImageTk.PhotoImage(img4)

chng2 = canvas4.create_image(0,0, anchor=NW, image=img4)

slave_devices = ["a", "b", "c"] # these are just dummy list components, do not worry about them

node_map1_val = StringVar()
node_map1 = ttk.OptionMenu(canvas4, node_map1_val, "", *slave_devices)
node_map1.config(width=18) #vary the width as per the need, dont keep too short
node_map1.place(x=100, y=100) #place the dropdowns on designated spots in a very organised manner with proper alignments

gui.mainloop()
