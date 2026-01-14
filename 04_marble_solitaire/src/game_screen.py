import pygame as pg
from values import screen_dims, colors

class GameScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.back_image = pg.transform.scale(pg.image.load("../resources/images/game_screen_image.png"),
                                             screen_dims).convert_alpha()

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.image, (0, 0))
