import pygame

from Display import Overlays, Window
from Event import Quit
from Person import Tree as PTree
from Setup import Constants as c, GlobalVars as gv

# Initialize pygame
pygame.init()
screen: pygame.Surface = pygame.display.set_mode(c.INIT_WINDOW_SIZE)
clock: pygame.time.Clock = pygame.time.Clock()
pygame.display.set_caption("Family Tree Maker")

# Initialise the Program
gv.family_tree = PTree.Tree()
Overlays.init()

while True:
    clock.tick(c.FPS)

    Quit.event_quit_check(pygame.event.get())

    Window.display(screen)
