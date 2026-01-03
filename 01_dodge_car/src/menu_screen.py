# Import necessary libraries
import pygame as pg
from button import Button

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)

class MenuScreen:
    def __init__(self, in_screen):
        # Font
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 60)
        self.button1 = Button("Start Game", (80, 40), (150, 200), GREEN, self.screen)
        self.button2 = Button("Quit Game", (80, 40), (150, 300), GREEN, self.screen)

    def draw_screen(self):
        self.screen.fill(RED)
        text_start = self.font.render('MENU', True, BLUE)
        rect_start = text_start.get_rect()
        rect_start.center = 150, 20
        self.screen.blit(text_start, rect_start)
        self.button1.draw_button()
        self.button2.draw_button()

