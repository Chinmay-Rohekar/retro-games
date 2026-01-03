import pygame as pg

class Button:
    def __init__(self, in_text, in_size, in_location, in_color, in_screen):
        self.font = pg.font.SysFont(None, 40)
        self.text = in_text
        self.size = in_size
        self.location = in_location
        self.color = in_color
        self.screen = in_screen
        self.text_button = self.font.render(self.text, True, self.color)
        self.rect_button = self.text_button.get_rect(center=self.location)

    def draw_button(self):
        self.screen.blit(self.text_button, self.rect_button)
