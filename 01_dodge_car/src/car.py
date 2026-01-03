import pygame as pg

BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Car:
    def __init__(self, in_type, in_pos):
        self.type = in_type
        self.pos = in_pos
        self.speed_y = 0

    def move_x(self, in_char):
        if in_char == 'a':
            self.pos[0] -= 100
            self.pos[0] = max(10, min(self.pos[0], 210))
        elif in_char == 'd':
            self.pos[0] += 100
            self.pos[0] = max(10, min(self.pos[0], 210))

    def move_y(self):
        self.pos[1] += self.speed_y

    def draw_car(self, in_screen):
        pg.draw.rect(in_screen, BLUE, (self.pos[0], self.pos[1], 80, 100))
