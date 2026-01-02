# Import necessary libraries
import pygame as pg

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)


# Font
font = pg.font.SysFont(None, 60)

class MenuScreen:
    def __init__(self):
        pass

    def draw_screen(self, in_screen):
        in_screen.fill(RED)
        text_start = font.render('START', True, BLUE)
        rect_start = text_start.get_rect()
        rect_start.center = 150, 250
        in_screen.blit(text_start, rect_start)

    def handle_event(self):
        return 'menu'

