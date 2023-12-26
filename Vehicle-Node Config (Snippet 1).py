# Do not make any changes in this code snippet, apart from resizing the UI image as instructed in the lines below
# Before you begin, import "Pillow" (version 9.3.0) package using your in-IDE package installer or through terminal using "pip install Pillow=9.3.0"
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

canvas4 = Canvas(gui, width=1535, height=1100, bg="Black", bd=0,
                 highlightthickness=0)  # Resize this and the LINE 19 equally, so as to fit the UI on your entire screen
gui.state('zoomed')
start_time5 = time.time()
canvas4.pack()

img4 = Image.open(
    r'C:\Users\Rezwan\Desktop\safear_internship\Quadcopter.png')  # Replace this path with the vehicle's image that you have been assigned for
img4 = img4.resize((1535, 800))
img4 = ImageTk.PhotoImage(img4)

chng2 = canvas4.create_image(0, 0, anchor=NW, image=img4)

frame_options = ['Select', 'Option 1', 'Option 2', 'Option 3']
# Positions for dropdowns according to the width and height of the image
image_width = 1535
image_height = 1100
frame_positions = {
    'top_left': (image_width * 0.12, image_height * 0.29),  # Adjust the multipliers to change the position
    'top_right': (image_width * 0.34, image_height * 0.29),  # dynamically according to the image size
    'bottom_left': (image_width * 0.12, image_height * 0.44),
    'bottom_right': (image_width * 0.34, image_height * 0.44),
}

# Place dropdowns on specified positions
dropdowns = {}
for name, (x, y) in frame_positions.items():
    var = StringVar(value=frame_options[0])
    dropdowns[name] = ttk.OptionMenu(gui, var, *frame_options)
    dropdowns[name].config(width=10)
    canvas4.create_window(x, y, window=dropdowns[name])

# Define options for the primary gimbal dropdowns
gimbal_options = {
    'wrist': ['Wrist', 'Option 1', 'Option 2'],
    'elbow': ['Elbow', 'Option 1', 'Option 2'],
    'shoulder_x': ['Shoulder X', 'Option 1', 'Option 2'],
    'shoulder_z': ['Shoulder Z', 'Option 1', 'Option 2']
}

# Define positions for the primary gimbal dropdowns
gimbal_positions = {
    'wrist': (image_width * 0.45, image_height * 0.27),
    'elbow': (image_width * 0.56, image_height * 0.29),
    'shoulder_x': (image_width * 0.60, image_height * 0.37),
    'shoulder_z': (image_width * 0.48, image_height * 0.42)
}

# Place primary gimbal dropdown menus
for name, options in gimbal_options.items():
    var = StringVar(value=options[0])
    dropdown = ttk.OptionMenu(gui, var, *options)
    dropdown.config(width=10)
    x, y = gimbal_positions[name]
    canvas4.create_window(x, y, window=dropdown)

# Define options for the secondary gimbal dropdowns
secondary_options = ['LL', 'UL']


# Function to clear the default text when the entry gains focus
def delete_text(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tkinter.END)


# Function to re-insert default text
def insert_default_text(event, entry, default_text):
    if entry.get().strip() == "":
        entry.insert(0, default_text)


# Place secondary gimbal text boxes directly under the primary ones
for name, primary_position in gimbal_positions.items():
    primary_x, primary_y = primary_position
    secondary_y = primary_y + 20  # Y offset from the primary dropdown to place the secondary ones below

    # Create two secondary text boxes for each primary
    for i, default_text in enumerate(secondary_options):
        textbox = Entry(canvas4, width=6)
        secondary_x = primary_x + (i * 50) - 45  # Adjust the multiplier for spacing, and offset to center
        textbox.place(x=secondary_x, y=secondary_y)
        textbox.insert(0, default_text)

        # Bind the delete_text function to the focus-in event
        textbox.bind("<FocusIn>", lambda event, e=textbox, d=default_text: delete_text(event, e, d))

        # Bind the insert_default_text function to the focus-out event
        textbox.bind("<FocusOut>", lambda event, e=textbox, d=default_text: insert_default_text(event, e, d))

gui.mainloop()
