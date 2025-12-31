import pygame as pg

BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Paddle:
    def __init__(self, in_type):
        self.type = in_type
        self.pos_x = 110
        if self.type == 'player':
            self.pos_y = 480
            self.color = BLUE
        else:
            self.pos_y = 70
            self.color = RED
        self.speed_x = 0.0
        self.speed_y = 0.0
        self.score = 0
        self.length = 50

    def draw_paddle(self, in_screen):
        pg.draw.rect(in_screen, self.color, (self.pos_x, self.pos_y, 80, 10), border_radius=5)

    def move(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        # Clamp the values within limits
        self.pos_x = max(5, min(self.pos_x, 215))
        if self.type == 'player':
            self.pos_y = max(300, min(self.pos_y, 480))
        else:
            self.pos_y = max(70, min(self.pos_y, 250))

    def get_rect(self):
        return pg.Rect(self.pos_x, self.pos_y, 80, 10)
