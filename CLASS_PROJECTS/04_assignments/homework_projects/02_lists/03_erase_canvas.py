import tkinter as tk
from tkinter import colorchooser

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 450
CELL_SIZE = 30
ERASE_SIZE = 1

color = "#ff0000"  # Default Color


def choose_color():
    global color  # Make GLobal
    # Chose Color and get first index
    color = colorchooser.askcolor(title="Select a Color")[1]
    title_text.config(bg=color)


def erase(event):
    # Get Mouse Position
    x, y = event.x, event.y
    # Find Object ID Number Return as "TUPLE"
    overlap = canvas.find_overlapping(x, y, x+ERASE_SIZE, y+ERASE_SIZE)
    # Loop "TUPLE"
    for obj in overlap:
        # Updated Below Info
        canvas.itemconfig(obj, fill=color, outline=color)


def undo(event):
    # Get Mouse Position
    x, y = event.x, event.y
    # Find Object ID Number Return as "TUPLE"
    overlap = canvas.find_overlapping(x, y, x+ERASE_SIZE, y+ERASE_SIZE)
    # Loop "TUPLE
    for obj in overlap:
        # Updated Below Info
        canvas.itemconfig(obj, fill="white", outline="lightgray",)


def reset_btn():
    # Find all Object in the Canvas
    for obj in canvas.find_all():
        # Updated Below Info
        canvas.itemconfig(obj, fill="white", outline="lightgray",)


root = tk.Tk()  # Initialize Root Window
root.title("Erase Canvas by Zubair Ahmed")  # Title


canvas = tk.Canvas(root, width=CANVAS_WIDTH,
                   height=CANVAS_HEIGHT, bg="lightgray")  # Main Canvas
canvas.pack(padx=10, pady=10)  # Render Canvas

# Create Cell
for row in range(0, CANVAS_WIDTH, CELL_SIZE):
    for col in range(0, CANVAS_HEIGHT, CELL_SIZE):
        canvas.create_rectangle(
            row, col, row + CELL_SIZE, col + CELL_SIZE, fill="white", outline="lightgray", dash=1)

# Details
details = tk.Label(
    root, text=" Fill: L-Click / Drag\t Erase: R-Click / Drag")
details.pack()

# Color Button
color_button = tk.Button(text="Pick a Color", bg="#171717", fg="white", activebackground="#601be0", activeforeground="white",  pady=7,
                         padx=20, command=choose_color, )
color_button.pack(side="left", pady=10, padx=10)

# Selected Color Box
title_text = tk.Label(root, text="",
                      bg=color, width=4, height=2)
title_text.pack(side="left")

# Undo Button
undo_button = tk.Button(text="Undo All", bg="#f21d28",
                        fg="white", activebackground="#601be0", activeforeground="white", pady=7, padx=20, command=reset_btn)  # Undo Button
undo_button.pack(side="right", pady=10, padx=10)  # Render Undo Button

# Button Types
canvas.bind("<B1-Motion>", erase)  # Mouse Left Click + Drag
canvas.bind("<Button-1>", erase)  # Mouse Left Click
canvas.bind("<B3-Motion>", undo)  # Mouse Right Click + Drag
canvas.bind("<Button-3>", undo)  # Mouse Right Click


root.mainloop()  # Render Window
