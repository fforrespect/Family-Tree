import pygame
from typing import Literal

from Person import Create, Tree, PersonalInfo
from Setup import Constants as c, GlobalVars as gv, Colours


def init():
    Title()


class Title:
    def __init__(self):
        self.loc: tuple[int, int] = (c.INIT_WINDOW_SIZE[0]//2, 30)
        self.text: str = "Family Tree"
        self.colour: tuple[int, int, int] = Colours.WHITE

        gv.all_objects.append(self)

    def draw(self, screen: pygame.Surface):
        title_font = pygame.font.Font(None, 30)
        title = title_font.render(self.text, True, self.colour)
        title_rect = title.get_rect()
        title_rect.center = self.loc

        screen.blit(title, title_rect)

