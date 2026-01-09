import pygame as pg

class Button:
    def __init__(self, in_screen, in_text, in_text_size, in_text_color, in_location, in_size,
                 in_bg_color, in_border_color, in_hover_bg_color):
        self.screen = in_screen
        self.text = in_text
        self.font = pg.font.Font(None, in_text_size)
        self.text_color = in_text_color
        self.location = in_location
        self.size = in_size
        self.bg_color = in_bg_color
        self.border_color = in_border_color
        self.hover_bg_color = in_hover_bg_color
        self.button_text = self.font.render(self.text, True, self.text_color)
        self.button_rect = self.button_text.get_rect(center=self.location)
        x, y = self.location
        size_x, size_y = self.size
        self.rect = pg.Rect(x-(size_x//2), y-(size_y//2), size_x, size_y)
        self.hover_state = False

    def draw_button(self):
        if self.hover_state:
            pg.draw.rect(self.screen, self.hover_bg_color, self.rect, border_radius=5)
            pg.draw.rect(self.screen, self.border_color, self.rect, width=2, border_radius=5)
            self.screen.blit(self.button_text, self.button_rect)
        else:
            pg.draw.rect(self.screen, self.bg_color, self.rect, border_radius=10)
            pg.draw.rect(self.screen, self.border_color, self.rect, width=2, border_radius=5)
            self.screen.blit(self.button_text, self.button_rect)
