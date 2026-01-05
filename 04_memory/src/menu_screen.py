# Import necessary libraries
import pygame as pg
from button import Button
from colors import colors, screen_dims

class MenuScreen:
    def __init__(self, in_screen):
        # Font
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 60)
        self.button1 = Button("Start Game", (170, 60), (screen_dims['width']/2, 200), colors['GREEN'],
                              colors['GRAY'], self.screen, 40)
        self.button2 = Button("Quit Game", (170, 60), (screen_dims['width']/2, 300), colors['GREEN'],
                              colors['GRAY'], self.screen, 40)

    def draw_screen(self):
        self.screen.fill(colors['RED'])
        text_start = self.font.render('MENU', True, colors['BLUE'])
        rect_start = text_start.get_rect()
        rect_start.center = 150, 20
        self.screen.blit(text_start, rect_start)
        self.button1.draw_button()
        self.button2.draw_button()

