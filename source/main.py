import tkinter as tk

from Display import Overlays, Tree
from Setup import Constants as c

# Initialize Tkinter
window: tk.Tk = tk.Tk()
window.title("Family Tree")
window.geometry(f"{c.INIT_WINDOW_WIDTH}x{c.INIT_WINDOW_HEIGHT}")

Overlays.draw(window)
Tree.draw(window)

# Start the application
window.mainloop()
