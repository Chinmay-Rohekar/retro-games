import pygame as pg
from values import colors

class GameBoard:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.grid = [[-2, -2, 1, 1, 1, -2, -2],
                     [-2, -2, 1, 1, 1, -2, -2],
                     [ 1,  1, 1, 1, 1,  1,  1],
                     [ 1,  1, 1, 0, 1,  1,  1],
                     [ 1,  1, 1, 1, 1,  1,  1],
                     [-2, -2, 1, 1, 1, -2, -2],
                     [-2, -2, 1, 1, 1, -2, -2] ]
        self.marble_image = pg.transform.scale(pg.image.load("../resources/images/marble_blue_tp.png"),
                                               (30, 30)).convert_alpha()

        self.points = [[None,       None,       (163, 166), (200, 166), (237, 166), None,       None],
                       [None,       None,       (163, 198), (200, 198), (237, 198), None,       None],
                       [( 87, 230), (125, 230), (163, 230), (200, 230), (237, 230), (275, 230), (313, 230)],
                       [( 87, 265), (125, 265), (163, 265), (200, 265), (237, 265), (275, 265), (314, 265)],
                       [( 87, 300), (125, 300), (163, 300), (200, 300), (237, 300), (275, 300), (314, 300)],
                       [None,       None,       (163, 332), (200, 332), (237, 332), None,       None],
                       [None,       None,       (163, 368), (200, 368), (237, 368), None,       None]]

    def draw_board(self):
        for i in range(7):
            for j in range(7):
                if self.points[i][j] is not None:
                    if self.grid[i][j] == 1:
                        self.screen.blit(self.marble_image,
                                         (self.points[i][j][0]-15, self.points[i][j][1]-15))

