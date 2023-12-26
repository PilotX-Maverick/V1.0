import tkinter as Tk
from tkinter import *
from tkinter import ttk
import time
from PIL import Image, ImageTk

# List of devices for Satellite screen (customize as needed)
list_of_devices_for_satellite = ["Device1", "Device2", "Device3"]

gui = Tk()
gui.geometry('1250x1080')
gui.config(bg="grey")
gui.title('Planner X - Developer 1.0.1')

canvas4 = Canvas(gui, width=1535, height=1100, bg="Black", bd=0, highlightthickness=0)
gui.state('zoomed')
start_time5 = time.time()
canvas4.pack()

# Load the image for the Satellite screen
img4 = Image.open(r'C:\Users\User\Desktop\AUTO PILOT\Mapping\Satellite.png')
img4 = img4.resize((1535, 800))
img4 = ImageTk.PhotoImage(img4)

chng2 = canvas4.create_image(0, 0, anchor=NW, image=img4)

slave_devices = ["a", "b", "c"]

# Existing Quadcopter dropdown
quadcopter_node_val = StringVar()
quadcopter_node = ttk.OptionMenu(canvas4, quadcopter_node_val, "", *slave_devices)
quadcopter_node.config(width=18)
quadcopter_node.place(x=100, y=100)

# New Satellite dropdown
satellite_node_val = StringVar()
satellite_node = ttk.OptionMenu(canvas4, satellite_node_val, "", *list_of_devices_for_satellite)
satellite_node.config(width=18)
satellite_node.place(x=200, y=150)  # Adjust the coordinates as needed for proper alignment

gui.mainloop()
