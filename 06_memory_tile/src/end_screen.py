import pygame as pg
from values import screen_dims, colors

class EndScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.back_image_path = "..//resources//images//end_screen_image.png"
        self.back_image = pg.transform.scale(pg.image.load(self.back_image_path), screen_dims)

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.image, (0, 0))