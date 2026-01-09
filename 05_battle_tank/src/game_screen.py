import pygame as pg
from button import Button
from values import colors, screen_dims

class GameScreen:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.font = pg.font.SysFont(None, 30)
        self.image = pg.transform.scale(pg.image.load("..//resources//game_screen_image.png"),
                                        screen_dims).convert_alpha()
        self.image.set_alpha(200)
        self.score_text = self.font.render("SCORE: 0", True, colors['WARM_GOLD'])
        self.score_rect = self.score_text.get_rect(center=(screen_dims[0] // 2, 25))
        self.home_image = pg.transform.scale(pg.image.load("..//resources//home_icon.png"),
                                             (40, 40))
        self.pause_image = pg.transform.scale(pg.image.load("..//resources//pause_icon.png"),
                                             (40, 40))
        self.tank_image = pg.transform.scale(pg.image.load("..//resources//tank_red.png"),
                                             (75, 120))

    def draw_screen(self):
        self.screen.fill(colors['WHITE'])
        self.screen.blit(self.image, (0, 0))
        # pg.draw.rect(self.screen, colors['BLACK'], (0, 0, screen_dims[0], 50))
        pg.draw.rect(self.screen, colors['BLACK'], (screen_dims[0]//2 - 90, 5, 180, 40), border_radius=10)
        pg.draw.rect(self.screen, colors['WARM_GOLD'], (screen_dims[0] // 2 - 90, 5, 180, 40),
                     width=3, border_radius=10)
        pg.draw.rect(self.screen, colors['BLACK'], rect=(10, 5, 40, 40), border_radius=5)
        pg.draw.rect(self.screen, colors['BLACK'], rect=(250, 5, 40, 40), border_radius=5)
        self.screen.blit(self.home_image, (250, 5))
        self.screen.blit(self.pause_image, (10, 5))
        self.screen.blit(self.tank_image, (150, 250))
        self.screen.blit(self.score_text, self.score_rect)

    def start_music(self):
        pg.mixer.music.load("..//resources//music//game_screen_music.mp3")
        pg.mixer.music.set_volume(0.5)  # 0.0 to 1.0
        pg.mixer.music.play(-1)

    def stop_music(self):
        pg.mixer.music.stop()


