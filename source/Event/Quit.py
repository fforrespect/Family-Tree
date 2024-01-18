import pygame


def event_quit_check(events: list[pygame.event.Event]):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
