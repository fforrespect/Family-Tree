import pygame as pg

from Display import Overlays, Tree
from Person import Tree as PTree
from Setup import Constants as c, GlobalVars as gv

# Initialize Tkinter
# window: tk.Tk = tk.Tk()
# window.title("Family Tree")
# window.geometry(f"{c.INIT_WINDOW_SIZE[0]}x{c.INIT_WINDOW_SIZE[1]}")

# Initialise the Tree
gv.family_tree = PTree.Tree()

# Overlays.draw(window)
# Tree.draw(window)
#
# # Start the application
# window.mainloop()
