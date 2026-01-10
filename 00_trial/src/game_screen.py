import pygame as pg
from button import Button

MENU = "menu"
SETTINGS = "settings"

class GameScreen:
    def __init__(self, in_font):
        self.menu_btn = Button("Menu", (200, 120), in_font)
        self.settings_btn = Button("Settings", (200, 180), in_font)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.menu_btn.clicked(event.pos_x):
                return MENU
            if self.settings_btn.clicked(event.pos_x):
                return SETTINGS

    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.menu_btn.draw(screen)
        self.settings_btn.draw(screen)
