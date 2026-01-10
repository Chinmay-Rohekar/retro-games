import pygame as pg

class EnemyShell:
    def __init__(self, in_screen, in_pos_x, in_pos_y):
        self.screen = in_screen
        self.image = pg.transform.scale(pg.image.load("../resources/images/shell_red.png"),
                                        (12, 40))
        self.state = False
        self.pos_x = in_pos_x
        self.pos_y = in_pos_y

    def draw_shell(self):
        self.screen.blit(self.image, ((self.pos_x*75) + 31, self.pos_y))
