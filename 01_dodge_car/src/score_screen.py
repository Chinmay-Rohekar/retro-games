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
    def __init__(self, in_screen):
        # Font
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 60)
        self.button1 = Button("Main Menu", (80, 40), (150, 150), GREEN, self.screen)
        self.button2 = Button("Restart Game", (80, 40), (150, 250), GREEN, self.screen)
        self.button3 = Button("Quit Game", (80, 40), (150, 350), GREEN, self.screen)
        self.fin_score = 0

    def draw_screen(self):
        self.screen.fill(RED)
        text_start = self.font.render('GAME OVER', True, BLUE)
        rect_start = text_start.get_rect()
        rect_start.center = 150, 30
        self.screen.blit(text_start, rect_start)
        text_score = self.font.render("SCORE: " + str(self.fin_score), True, BLUE)
        rect_score = text_score.get_rect()
        rect_score.center = 150, 90
        self.screen.blit(text_score, rect_score)
        self.button1.draw_button()
        self.button2.draw_button()
        self.button3.draw_button()

