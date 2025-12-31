import pygame as pg
from button import Button

MENU = "menu"
SETTINGS = "settings"
QUIT = "quit"

class SettingsScreen:
    def __init__(self, in_font):
        self.back_btn = Button("Back", (200, 120), in_font)
        self.quit_btn = Button("Quit", (200, 180), in_font)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.back_btn.clicked(event.pos):
                return MENU
            if self.quit_btn.clicked(event.pos):
                return QUIT

    def draw(self, screen):
        screen.fill((50, 200, 100))
        self.back_btn.draw(screen)
        self.quit_btn.draw(screen)
