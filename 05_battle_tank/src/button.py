import pygame as pg

class Button:
    def __init__(self, in_screen, in_text, in_size, in_location, in_bg_color, in_text_color,
                 in_hover_text_color, in_hover_bg_color):
        self.font = pg.font.SysFont(None, 40)
        self.screen = in_screen
        self.text = in_text
        self.size = in_size
        self.location = in_location
        self.bg_color = in_bg_color
        self.text_color = in_text_color
        self.text_button = self.font.render(self.text, True, self.text_color)
        self.rect_button = self.text_button.get_rect(center=self.location)
        self.hover = False
        self.hover_text_color = in_hover_text_color
        self.hover_bg_color = in_hover_bg_color

    def draw_button(self):
        if self.hover:
            self.text_button = self.font.render(self.text, True, self.hover_text_color)
            self.rect_button = self.text_button.get_rect(center=self.location)
            self.screen.blit(self.text_button, self.rect_button)
        else:
            self.screen.blit(self.text_button, self.rect_button)
