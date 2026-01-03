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

class GameScreen:
    def __init__(self, in_screen):
        # Font
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 40)
        self.button1 = Button("Menu", (80, 40), (50, 30), GREEN, self.screen)
        self.button2 = Button("Pause", (80, 40), (250, 30), GREEN, self.screen)

    def draw_screen(self):
        self.screen.fill(RED)
        pg.draw.rect(self.screen, GRAY, (0, 0, 300, 60))
        text_start = self.font.render('GAME', True, BLUE)
        rect_start = text_start.get_rect()
        rect_start.center = 150, 80
        text_score = self.font.render('SCORE', True, BLUE)
        rect_score = text_score.get_rect()
        rect_score.center = 150, 15
        self.screen.blit(text_score, rect_score)
        self.button1.draw_button()
        self.button2.draw_button()

    def draw_score(self, in_score):
        text_score_val = self.font.render(str(in_score), True, BLUE)
        rect_score_val = text_score_val.get_rect()
        rect_score_val.center = 150, 45
        self.screen.blit(text_score_val, rect_score_val)
