import pygame as pg

class Shell:
    def __init__(self, in_screen, in_pos_x, in_pos_y, in_type):
        self.screen = in_screen
        self.type = in_type
        if in_type == 'p':
            self.image = pg.transform.scale(pg.image.load("..//resources//shell_blue.png"),
                                                  (12, 40))
        elif in_type == 'e':
            self.image = pg.transform.scale(pg.image.load("..//resources//shell_red.png"),
                                                  (12, 40))
        self.state = False
        self.pos_x = in_pos_x
        self.pos_y = in_pos_y

    def draw_shell(self):
        self.screen.blit(self.image, ((self.pos_x*75) + 31, self.pos_y))
