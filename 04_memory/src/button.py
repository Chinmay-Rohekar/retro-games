import pygame as pg

class Button:
    def __init__(self, in_text, in_size, in_location, in_text_color, in_bg_color,
                 in_screen, in_font_size):
        self.font = pg.font.SysFont(None, in_font_size)
        self.text = in_text
        self.size = in_size
        self.location = in_location
        self.text_color = in_text_color
        self.bg_color = in_bg_color
        self.screen = in_screen
        self.text_button = self.font.render(self.text, True, self.text_color)
        self.rect_button = self.text_button.get_rect(center=self.location)

    def draw_button(self):
        a = self.location[0]
        b = self.location[1]
        c = self.size[0]
        d = self.size[1]
        pg.draw.rect(self.screen, self.bg_color, (a-(c/2), b-(d/2), c, d),
                     border_radius=15)
        self.screen.blit(self.text_button, self.rect_button)
