import pygame as pg
from values import colors, screen_dims, settings_circles
import values

class SettingsScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.back_image = pg.transform.scale(pg.image.load("../resources/images/settings_screen_image.png"),
                                             screen_dims).convert_alpha()
        self.tick_image = pg.transform.scale(pg.image.load("..//resources//images//green_check.png"),(50, 50))
        self.music_file = "..//resources//music//game_screen_music.mp3"


    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.back_image, (0, 0))
        if values.music_on:
            self.screen.blit(self.tick_image, (255, 205))
        pg.draw.circle(self.screen, colors['RED'],
                       (settings_circles[values.marble_color][0], settings_circles[values.marble_color][1]),
                       settings_circles[values.marble_color][2], 5)

    def start_music(self):
        if values.music_on:
            pg.mixer.music.load(self.music_file)
            pg.mixer.music.set_volume(0.2)  # 0.0 to 1.0
            pg.mixer.music.play(-1)

    def stop_music(self):
        pg.mixer.music.stop()

