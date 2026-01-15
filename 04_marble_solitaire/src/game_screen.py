import pygame as pg
from values import screen_dims, colors
from game_board import GameBoard

class GameScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.back_image = pg.transform.scale(pg.image.load("../resources/images/game_screen_image.png"),
                                             screen_dims).convert_alpha()
        self.music_file = "..//resources//music//game_screen_music.mp3"
        self.game_board = GameBoard(self.screen)

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.back_image, (0, 0))
        self.game_board.draw_board()

    def start_music(self):
        pg.mixer.music.load(self.music_file)
        pg.mixer.music.set_volume(0.5)  # 0.0 to 1.0
        pg.mixer.music.play(-1)

    def stop_music(self):
        pg.mixer.music.stop()

    def handle_mouse_clicks(self, in_mouse_pos):
        self.game_board.handle_mouse_clicks(in_mouse_pos)
