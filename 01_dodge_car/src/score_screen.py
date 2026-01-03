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

class ScoreScreen:
    def __init__(self, in_screen, in_fin_score):
        # Font
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 60)
        self.button1 = Button("Main Menu", (80, 40), (150, 150), GREEN, self.screen)
        self.button2 = Button("Restart Game", (80, 40), (150, 250), GREEN, self.screen)
        self.button3 = Button("Quit Game", (80, 40), (150, 350), GREEN, self.screen)
        self.final_score = in_fin_score

    def draw_screen(self):
        self.screen.fill(RED)
        text_start = self.font.render('GAME OVER', True, BLUE)
        rect_start = text_start.get_rect()
        rect_start.center = 150, 20
        self.screen.blit(text_start, rect_start)
        self.button1.draw_button()
        self.button2.draw_button()
        self.button3.draw_button()
