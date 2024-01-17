import tkinter as tk

from Setup import Constants as c


def draw_line():
    canvas.delete("all")  # Clear existing line
    canvas.create_line(0, 0, window.winfo_width(), 0, width=1)  # Draw new line


# Initialize Tkinter
window = tk.Tk()
window.title("Family Tree")
window.geometry(f"{c.INIT_WINDOW_WIDTH}x{c.INIT_WINDOW_HEIGHT}")

# Create a label
label = tk.Label(window, text="Family Tree", font=("Arial Bold", 20))
label.pack(side="top", anchor="center")

# Create a canvas for the line with a slightly larger height and optional background color
canvas = tk.Canvas(window, height=2, bg="gray")  # Background color is optional
canvas.pack(fill="x")

# Bind the resize event
window.bind("<Configure>", lambda e: draw_line())

# Start the application
window.mainloop()
