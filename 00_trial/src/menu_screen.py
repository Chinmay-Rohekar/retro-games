import pygame as pg
from button import Button

MENU = "menu"
SETTINGS = "settings"
GAME = "game"

class MenuScreen:
    def __init__(self, in_font):
        self.play_btn = Button("Play", (200, 120), in_font)
        self.settings_btn = Button("Settings", (200, 180), in_font)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.play_btn.clicked(event.pos_x):
                return GAME
            if self.settings_btn.clicked(event.pos_x):
                return SETTINGS

    def draw(self, screen):
        screen.fill((50, 100, 200))
        self.play_btn.draw(screen)
        self.settings_btn.draw(screen)
