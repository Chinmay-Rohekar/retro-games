import pygame as pg
from values import screen_dims, colors
from tile_board import TileBoard

class GameScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.back_image_path = "..//resources//images//game_screen_image.png"
        self.back_image = pg.transform.scale(pg.image.load(self.back_image_path), screen_dims)
        self.tile_board = TileBoard(self.screen)

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.back_image, (0, 0))
        self.tile_board.draw_board()

    def check_tile_collision(self, in_mouse_pos):
        self.tile_board.check_collision(in_mouse_pos)


