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
image_width = 1535
image_height = 1100

# Top left dropdown
node_map1_val = StringVar(value=frame_options[0])
node_map1 = ttk.OptionMenu(canvas4, node_map1_val, *frame_options)
node_map1.config(width=8)
node_map1.place(x=image_width * 0.10, y=image_height * 0.28)

# Top right dropdown
node_map2_val = StringVar(value=frame_options[0])
node_map2 = ttk.OptionMenu(canvas4, node_map2_val, *frame_options)
node_map2.config(width=8)
node_map2.place(x=image_width * 0.30, y=image_height * 0.28)

# Bottom left dropdown
node_map3_val = StringVar(value=frame_options[0])
node_map3 = ttk.OptionMenu(canvas4, node_map3_val, *frame_options)
node_map3.config(width=8)
node_map3.place(x=image_width * 0.10, y=image_height * 0.43)

# Bottom right dropdown
node_map4_val = StringVar(value=frame_options[0])
node_map4 = ttk.OptionMenu(canvas4, node_map4_val, *frame_options)
node_map4.config(width=8)
node_map4.place(x=image_width * 0.30, y=image_height * 0.43)

# Define options for the primary gimbal dropdowns
gimbal_options = {
    'wrist': ['Wrist', 'Option 1', 'Option 2'],
    'elbow': ['Elbow', 'Option 1', 'Option 2'],
    'shoulder_x': ['Shoulder X', 'Option 1', 'Option 2'],
    'shoulder_z': ['Shoulder Z', 'Option 1', 'Option 2']
}

# Wrist Gimbal Dropdown
node_map5_val = StringVar(value=gimbal_options['wrist'][0])
node_map5 = ttk.OptionMenu(canvas4, node_map5_val, *gimbal_options['wrist'])
node_map5.config(width=8)
node_map5.place(x=image_width * 0.43, y=image_height * 0.26)

# Elbow Gimbal Dropdown
node_map6_val = StringVar(value=gimbal_options['elbow'][0])
node_map6 = ttk.OptionMenu(canvas4, node_map6_val, *gimbal_options['elbow'])
node_map6.config(width=8)
node_map6.place(x=image_width * 0.53, y=image_height * 0.29)

# Shoulder X Gimbal Dropdown
node_map7_val = StringVar(value=gimbal_options['shoulder_x'][0])
node_map7 = ttk.OptionMenu(canvas4, node_map7_val, *gimbal_options['shoulder_x'])
node_map7.config(width=8)
node_map7.place(x=image_width * 0.57, y=image_height * 0.36)

# Shoulder Z Gimbal Dropdown
node_map8_val = StringVar(value=gimbal_options['shoulder_z'][0])
node_map8 = ttk.OptionMenu(canvas4, node_map8_val, *gimbal_options['shoulder_z'])
node_map8.config(width=8)
node_map8.place(x=image_width * 0.46, y=image_height * 0.42)


# Function to clear the default text when the entry gains focus
def delete_text(event):
    if event.widget.get() == event.widget.default_text:
        event.widget.delete(0, Tk.END)

# Function to insert again default text
def insert_default_text(event):
    if event.widget.get().strip() == "":
        event.widget.insert(0, event.widget.default_text)


# Wrist Position Text Boxes
wrist_position_x = image_width * 0.43
wrist_position_y = image_height * 0.27 + 20

textbox1 = Entry(canvas4, width=5)
textbox1.place(x=wrist_position_x, y=wrist_position_y)
textbox1.insert(0, "LL")
textbox1.default_text = "LL"
textbox1.bind("<FocusIn>", delete_text)
textbox1.bind("<FocusOut>", insert_default_text)

textbox2 = Entry(canvas4, width=5)
textbox2.place(x=wrist_position_x + 45, y=wrist_position_y)
textbox2.insert(0, "UL")
textbox2.default_text = "UL"
textbox2.bind("<FocusIn>", delete_text)
textbox2.bind("<FocusOut>", insert_default_text)

# Wrist Position Text Boxes
elbow_position_x = image_width * 0.53
elbow_position_y = image_height * 0.30 + 20

textbox3 = Entry(canvas4, width=5)
textbox3.place(x=elbow_position_x, y=elbow_position_y)
textbox3.insert(0, "LL")
textbox3.default_text = "LL"
textbox3.bind("<FocusIn>", delete_text)
textbox3.bind("<FocusOut>", insert_default_text)

textbox4 = Entry(canvas4, width=5)
textbox4.place(x=elbow_position_x + 45, y=elbow_position_y)
textbox4.insert(0, "UL")
textbox4.default_text = "UL"
textbox4.bind("<FocusIn>", delete_text)
textbox4.bind("<FocusOut>", insert_default_text)

# Shoulder X Position Text Boxes
shoulder_x_position_x = image_width * 0.57
shoulder_x_position_y = image_height * 0.37 + 20

textbox5 = Entry(canvas4, width=5)
textbox5.place(x=shoulder_x_position_x, y=shoulder_x_position_y)
textbox5.insert(0, "LL")
textbox5.default_text = "LL"
textbox5.bind("<FocusIn>", delete_text)
textbox5.bind("<FocusOut>", insert_default_text)

textbox6 = Entry(canvas4, width=5)
textbox6.place(x=shoulder_x_position_x + 45, y=shoulder_x_position_y)
textbox6.insert(0, "UL")
textbox6.default_text = "UL"
textbox6.bind("<FocusIn>", delete_text)
textbox6.bind("<FocusOut>", insert_default_text)

# Shoulder Z Position Text Boxes
shoulder_z_position_x = image_width * 0.46
shoulder_z_position_y = image_height * 0.43 + 20

textbox7 = Entry(canvas4, width=5)
textbox7.place(x=shoulder_z_position_x, y=shoulder_z_position_y)
textbox7.insert(0, "LL")
textbox7.default_text = "LL"
textbox7.bind("<FocusIn>", delete_text)
textbox7.bind("<FocusOut>", insert_default_text)

textbox8 = Entry(canvas4, width=5)
textbox8.place(x=shoulder_z_position_x + 45, y=shoulder_z_position_y)
textbox8.insert(0, "UL")
textbox8.default_text = "UL"
textbox8.bind("<FocusIn>", delete_text)
textbox8.bind("<FocusOut>", insert_default_text)


gui.mainloop()
