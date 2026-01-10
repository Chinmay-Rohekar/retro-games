import pygame as pg
from button import Button
from values import colors, screen_dims

class StartScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 60)
        self.button_start = Button(self.screen, "START GAME", 25, colors['WARM_GOLD'],
                                   (screen_dims[0]/2, 400), (180, 40), colors['DARK_GUNMETAL'],
                                   colors['STEEL'], colors['LIGHT_METAL'])
        self.button_quit = Button(self.screen, "QUIT GAME", 25, colors['WARM_GOLD'],
                                   (screen_dims[0]/2, 460), (180, 40), colors['DARK_GUNMETAL'],
                                   colors['STEEL'], colors['LIGHT_METAL'])
        self.button_start_rect = pg.Rect(60, 380, 180, 40)
        self.button_quit_rect = pg.Rect(60, 440, 180, 40)
        self.buttons = [self.button_start, self.button_quit]
        self.image = pg.transform.scale(pg.image.load("../resources/images/first_screen_image.png"),
                                        screen_dims)
        self.music_file = "..//resources//music//start_screen_music.mp3"

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.image, (0, 0))
        for button in self.buttons:
            button.draw_button()

    def start_music(self):
        pg.mixer.music.load(self.music_file)
        pg.mixer.music.set_volume(0.5)  # 0.0 to 1.0
        pg.mixer.music.play(-1)

    def stop_music(self):
        pg.mixer.music.stop()


