# Import necessary libraries
import pygame as pg
from button import Button
from colors import colors, screen_dims

class PauseScreen:
    def __init__(self, in_screen):
        # Font
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 60)
        self.button1 = Button("Resume Game", (170, 60), (screen_dims['width']/2, 200), colors['GREEN'],
                              colors['GRAY'], self.screen, 40)
        self.button2 = Button("Main Menu", (170, 60), (screen_dims['width']/2, 300), colors['GREEN'],
                              colors['GRAY'], self.screen, 40)
        self.button3 = Button("Quit Game", (170, 60), (screen_dims['width'] / 2, 400), colors['GREEN'],
                              colors['GRAY'], self.screen, 40)

    def draw_screen(self):
        self.screen.fill(colors['RED'])
        text_start = self.font.render('GAME', True, colors['BLUE'])
        rect_start = text_start.get_rect()
        rect_start.center = screen_dims['width']/2, 50
        self.screen.blit(text_start, rect_start)
        self.button1.draw_button()
        self.button2.draw_button()
        self.button3.draw_button()
