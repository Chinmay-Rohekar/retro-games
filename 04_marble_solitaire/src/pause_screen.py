import pygame as pg
from values import colors, screen_dims

class PauseScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.image = pg.transform.scale(pg.image.load("../resources/images/pause_screen_image.png"),
                                        screen_dims).convert_alpha()

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.image, (0, 0))

