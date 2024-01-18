import pygame
from Setup import Constants as c, GlobalVars as gv, Colours


def init():
    Title()


class Title:
    def __init__(self):
        self.loc: tuple[int, int] = (c.INIT_WINDOW_SIZE[0]//2, 20)
        self.text: str = "Family Tree"
        self.colour: tuple[int, int, int] = Colours.WHITE

        gv.all_objects.append(self)

    def draw(self, screen: pygame.Surface):
        title_font = pygame.font.SysFont("arial", int(self.loc[1]*1.5))
        title = title_font.render(self.text, True, self.colour)
        title_rect = title.get_rect()
        title_rect.center = self.loc

        pygame.draw.line(screen,
                         self.colour,
                         (0, self.loc[1]*2),
                         (c.INIT_WINDOW_SIZE[0], self.loc[1]*2)
                         )

        screen.blit(title, title_rect)

