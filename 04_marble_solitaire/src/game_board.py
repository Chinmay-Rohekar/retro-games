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

        self.marble_rects = []
        for i in range(7):
            temp = []
            for j in range(7):
                if self.points[i][j] is None:
                    temp.append(None)
                else:
                    temp.append([pg.Rect(self.points[i][j][0]-15, self.points[i][j][1]-15, 30, 30), (i, j)])
            self.marble_rects.append(temp)

        self.selected_marble = None
        self.possible_moves = []
        self.jumped_marbles = []


    def draw_board(self):
        for i in range(7):
            for j in range(7):
                if self.points[i][j] is not None:
                    if self.grid[i][j] == 1:
                        self.screen.blit(self.marble_image,
                                         (self.points[i][j][0]-15, self.points[i][j][1]-15))

    def handle_mouse_clicks(self, in_mouse_pos):
        for row in self.marble_rects:       # Get the Row inside the Marble Rectangles
            for rectangle_data in row:      # Get the Data of a Rectangle inside the Row
                if rectangle_data is not None:
                    rectangle = rectangle_data[0]     # Get the Rectangle coordinates inside the Rect Data
                    if rectangle.collidepoint(in_mouse_pos):
                        print(rectangle_data[1])
                        self.motion_analysis(rectangle_data)


    def motion_analysis(self, in_rectangle_data):
        if self.selected_marble is None:        # Currently no marble is selected
            self.selected_marble = in_rectangle_data
            rectangle = self.selected_marble[0]
            row = self.selected_marble[1][0]
            col = self.selected_marble[1][1]

            self.possible_moves = [(row, col-2), (row-2, col), (row, col+2), (row+2, col)]

            for move in self.possible_moves[:]:
                if 0 <= move[0] <= 6 and 0 <= move[1] <= 6:
                    pass
                else:
                    self.possible_moves.remove(move)

            for move in self.possible_moves[:]:
                if self.grid[move[0]][move[1]] != 0:
                    self.possible_moves.remove(move)

            self.jumped_marbles = []
            for move in self.possible_moves:
                if move[0] == self.selected_marble[1][0]:
                    self.jumped_marbles.append((move[0], (move[1]+self.selected_marble[1][1])//2))
                elif move[1] == self.selected_marble[1][1]:
                    self.jumped_marbles.append(((move[0]+self.selected_marble[1][1])//2, move[1]))

        else:       # Marble has been selected
            clicked_rect = in_rectangle_data[0]
            clicked_row = in_rectangle_data[1][0]
            clicked_col = in_rectangle_data[1][1]

            for i in range(len(self.possible_moves)):
                move = self.possible_moves[i]
                jump = self.jumped_marbles[i]
                if move[0] == clicked_row and move[1] == clicked_col:
                    print("Here: {},{}".format(self.selected_marble[1][0], self.selected_marble[1][1]))
                    self.grid[move[0]][move[1]] = 1
                    self.grid[self.selected_marble[1][0]][self.selected_marble[1][1]] = 0
                    self.grid[jump[0]][jump[1]] = 0

            # for move in self.possible_moves:
            #     if move[0] == clicked_row and move[1] == clicked_col:
            #         print("Here: {},{}".format(self.selected_marble[1][0], self.selected_marble[1][1]))
            #         self.grid[move[0]][move[1]] = 1
            #         self.grid[self.selected_marble[1][0]][self.selected_marble[1][1]] = 0

            self.selected_marble = None



