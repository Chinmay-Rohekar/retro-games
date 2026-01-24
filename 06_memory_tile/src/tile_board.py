import pygame as pg
from values import colors
from tile import Tile
from random import shuffle
import values

class TileBoard:
    def __init__(self, in_screen):
        self.screen = in_screen
        self.card_back_side_path = "..//resources//images//tile_back.png"
        self.card_back_side_image = pg.transform.scale(pg.image.load(self.card_back_side_path),
                                                       (60, 80)).convert_alpha()
        # Create the tiles
        arr = list(range(1, 17))
        shuffle(arr)
        self.tiles = []
        for i in range(4):
            temp_row = []
            for j in range(4):
                tile = Tile(arr.pop() % 8, (i, j))
                temp_row.append(tile)
            self.tiles.append(temp_row)

        self.pos = [[(35, 170), (125, 170), (215, 170), (305, 170)],
                    [(35, 274), (125, 274), (215, 274), (305, 274)],
                    [(35, 378), (125, 378), (215, 378), (305, 378)],
                    [(35, 482), (125, 482), (215, 482), (305, 482)]]
        self.tile_rects = []
        for i in range(4):
            temp_row = []
            for j in range(4):
                temp_rect = pg.Rect(self.pos[i][j][0], self.pos[i][j][1], 60, 80)
                temp_row.append(temp_rect)
            self.tile_rects.append(temp_row)
        self.tiles_selected = []
        self.flip_time = 0
        self.tiles_unmatched = False

    def draw_board(self):
        for i in range(4):
            for j in range(4):
                if self.tiles[i][j].status == 0:
                    self.screen.blit(self.card_back_side_image, self.pos[i][j])
                elif self.tiles[i][j].status == 1:
                    self.screen.blit(self.tiles[i][j].image, self.pos[i][j])
                elif self.tiles[i][j].status == 2:
                    pg.draw.rect(self.screen, colors['RED'], self.tile_rects[i][j], width=5, border_radius=8)

    def check_collision(self, in_mouse_pos):
        for i in range(4):
            for j in range(4):
                # Collision has been detected
                if self.tile_rects[i][j].collidepoint(in_mouse_pos):
                    # No tile was selected yet
                    if len(self.tiles_selected) == 0:
                        # Flip the tile
                        self.tiles[i][j].status = 1
                        # Add the tile to the selected tiles list
                        self.tiles_selected.append(self.tiles[i][j])

                    # One tile has already been selected
                    elif len(self.tiles_selected) == 1:
                        self.tiles[i][j].status = 1
                        # Add the tile to the selected tiles list
                        self.tiles_selected.append(self.tiles[i][j])
                        # Both the selected tiles are same
                        if self.tiles_selected[0].image_num == self.tiles_selected[1].image_num:
                            print("Pair Found")
                            self.pair_animation()
                            self.tiles_selected[0].status = 2
                            self.tiles_selected[1].status = 2
                        else:
                            print("Not a Pair")
                            self.reset_unmatched_tiles()
                            self.tiles_unmatched = True
                            self.tiles_selected[0].status = 0
                            self.tiles_selected[1].status = 0

                        self.tiles_selected.pop()

    def reset_unmatched_tiles(self):
        pass

    def pair_animation(self):
        pass
