import tkinter as tk

from Person import Create
from Setup import GlobalVars as gv


def draw(window: tk.Tk):
    # Create a label
    label = tk.Label(window, text="Family Tree", font=("Arial Bold", 20))
    label.pack(side="top", anchor="center")

    # Create a canvas for the line with a slightly larger height and optional background color
    canvas = tk.Canvas(window, height=2, bg="gray")  # Background color is optional
    canvas.pack(fill="x")

    # Bind the resize event
    window.bind("<Configure>", lambda e: __draw_line(window, canvas))

    gv.family_tree.root = Create.new_person()


def __draw_line(window: tk.Tk, canvas: tk.Canvas):
    canvas.delete("all")  # Clear existing line
    canvas.create_line(0, 0, window.winfo_width(), 0, width=1)  # Draw new line
