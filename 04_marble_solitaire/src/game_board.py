import pygame as pg
from values import colors, screen_dims

class GameBoard:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.font = pg.font.Font(None, 45)
        self.grid = [[-2, -2, 1, 1, 1, -2, -2],
                     [-2, -2, 1, 1, 1, -2, -2],
                     [ 1,  1, 1, 1, 1,  1,  1],
                     [ 1,  1, 1, 0, 1,  1,  1],
                     [ 1,  1, 1, 1, 1,  1,  1],
                     [-2, -2, 1, 1, 1, -2, -2],
                     [-2, -2, 1, 1, 1, -2, -2] ]
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

        self.marble_image = pg.transform.scale(pg.image.load("../resources/images/marble_blue_tp.png"),
                                               (30, 30)).convert_alpha()
        self.win_image = pg.transform.scale(pg.image.load("..//resources//images//menu_win.png"),
                                            (300, 400)).convert_alpha()
        self.lose_image = pg.transform.scale(pg.image.load("..//resources//images//menu_lost.png"),
                                            (300, 400)).convert_alpha()

        self.selected_marble = None
        self.possible_moves = []
        self.jumped_marbles = []
        self.marble_count = 32
        self.move_count = 0
        self.game_state = 'on'
        self.game_timer = 0

    def draw_board(self):
        for i in range(7):
            for j in range(7):
                if self.points[i][j] is not None:
                    if self.grid[i][j] == 1:
                        self.screen.blit(self.marble_image,
                                         (self.points[i][j][0]-15, self.points[i][j][1]-15))

        move_text = self.font.render("{}".format(self.move_count), True, colors['RED'])
        move_rect = move_text.get_rect(center=(180, 492))
        self.screen.blit(move_text, move_rect)

        # When the Game has ended show the menu image on the top
        if self.game_state == 'off':
            if self.marble_count == 1:
                # Show the win menu
                self.screen.blit(self.win_image, (50, 100))
            else:
                # Show the lost menu
                self.screen.blit(self.lose_image, (50, 100))

        # Draw the selected Marble a bit bigger
        if self.selected_marble is not None:
            rectangle = self.selected_marble[0]
            big_marble_img = pg.transform.scale(pg.image.load("..//resources//images//marble_blue_tp.png"),
                                                (38, 38)).convert_alpha()
            self.screen.blit(big_marble_img, (rectangle[0]-4, rectangle[1]-4))
            # pg.draw.rect(self.screen, colors['RED'], self.selected_marble[0], width=3)

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
            row = self.selected_marble[1][0]
            col = self.selected_marble[1][1]

            # Check that the selected position actually has a marble
            if self.grid[row][col] == 1:
                self.possible_moves = [((row, col-2), (row, col-1)), ((row-2, col), (row-1, col)),
                                       ((row, col+2), (row, col+1)), ((row+2, col), (row+1, col))]

                # Check that the possible moves lie within the board
                for move in self.possible_moves[:]:
                    if 0 <= move[0][0] <= 6 and 0 <= move[0][1] <= 6:
                        pass
                    else:
                        self.possible_moves.remove(move)

                # Check that the possible moves are indeed empty
                for move in self.possible_moves[:]:
                    if self.grid[move[0][0]][move[0][1]] != 0:
                        self.possible_moves.remove(move)

                # Check that there exists a marble between the possible move
                for move in self.possible_moves[:]:
                    if self.grid[move[1][0]][move[1][1]] != 1:
                        self.possible_moves.remove(move)

            else:
                self.selected_marble = None
                return

        else:       # Marble has already been selected and now you are looking to place it somewhere
            clicked_rect = in_rectangle_data[0]
            clicked_row = in_rectangle_data[1][0]
            clicked_col = in_rectangle_data[1][1]

            for i in range(len(self.possible_moves)):
                move = self.possible_moves[i][0]
                jump = self.possible_moves[i][1]
                if move[0] == clicked_row and move[1] == clicked_col:
                    self.grid[move[0]][move[1]] = 1
                    self.grid[self.selected_marble[1][0]][self.selected_marble[1][1]] = 0
                    self.grid[jump[0]][jump[1]] = 0
                    self.move_count += 1

            self.selected_marble = None
            if not self.check_if_move_possible():
                self.game_state = 'off'
                if self.marble_count == 1:
                    print("You Win")
                else:
                    print("You Lose")


    def check_if_move_possible(self):
        # This function checks that there exists at least one move in the system
        self.marble_count = 0
        for row in range(7):
            for col in range(7):
                possible_moves = []
                if self.grid[row][col] == 1:
                    self.marble_count += 1
                    possible_moves = [((row, col - 2), (row, col - 1)), ((row - 2, col), (row - 1, col)),
                                      ((row, col + 2), (row, col + 1)), ((row + 2, col), (row + 1, col))]

                # Check that the possible moves lie within the board
                for move in possible_moves[:]:
                    if 0 <= move[0][0] <= 6 and 0 <= move[0][1] <= 6:
                        pass
                    else:
                        possible_moves.remove(move)

                # Check that the possible moves are indeed empty
                for move in possible_moves[:]:
                    if self.grid[move[0][0]][move[0][1]] != 0:
                        possible_moves.remove(move)

                # Check that there exists a marble between the possible move
                for move in possible_moves[:]:
                    if self.grid[move[1][0]][move[1][1]] != 1:
                        possible_moves.remove(move)

                if len(possible_moves) > 0:
                    return True

        return False

