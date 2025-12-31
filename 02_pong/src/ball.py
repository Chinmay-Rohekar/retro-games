import pygame as pg
from random import choice

GREEN = (0, 255, 0)

class Ball:
    def __init__(self):
        self.pos_x = 150
        self.pos_y = 280
        self.speed_x = 0
        self.speed_y = 0
        self.pause_time = 0
        self.paused = False

    def move(self):
        if self.paused:
            if pg.time.get_ticks() - self.pause_time > 500:  # 1 second pause
                self.speed_x = choice([5, -5])
                self.speed_y = choice([5, -5])
                self.paused = False
            return
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Reverse direction on hitting side walls
        if self.pos_x == 15 or self.pos_x == 285:
            self.speed_x *= -1
        if self.pos_y == 75:    # Ball has hit the top border
            self.reset_ball()
            return 'player'
        if self.pos_y == 485:   # Ball has hit the bottom border
            self.reset_ball()
            return 'opponent'
        return None


    def draw_ball(self, in_screen):
        pg.draw.circle(in_screen, GREEN, (self.pos_x, self.pos_y), 10)

    def reset_ball(self):
        self.pos_x = 150
        self.pos_y = 280
        self.speed_x = choice([5, -5])
        self.speed_y = choice([5, -5])
        self.paused = True
        self.pause_time = pg.time.get_ticks()

    def get_rect(self):
        return pg.Rect(self.pos_x-10, self.pos_y-10, 20, 20)
