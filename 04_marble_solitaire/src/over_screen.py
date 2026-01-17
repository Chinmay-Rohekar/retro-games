import pygame as pg
from values import colors, screen_dims
import values

class OverScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.back_image_win = pg.transform.scale(pg.image.load("../resources/images/over_win_screen_image.png"),
                                                 screen_dims).convert_alpha()
        self.back_image_loss = pg.transform.scale(pg.image.load("../resources/images/over_lose_screen_image.png"),
                                                  screen_dims).convert_alpha()
        self.music_file = "..//resources//music//over_screen_music.mp3"
        self.win = False

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        if self.win:
            self.screen.blit(self.back_image_win, (0, 0))
        else:
            self.screen.blit(self.back_image_loss, (0, 0))

    def start_music(self):
        if values.music_on:
            pg.mixer.music.load(self.music_file)
            pg.mixer.music.set_volume(0.5)  # 0.0 to 1.0
            pg.mixer.music.play(-1)

    def stop_music(self):
        pg.mixer.music.stop()
