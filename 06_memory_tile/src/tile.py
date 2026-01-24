import pygame as pg

class Tile:
    def __init__(self, in_image_num, in_index):
        # Status is to define if the tile is flipped or not
        # 0: Not Flipped, 1: Flipped, 2: Discarded
        self.status = 0
        # There are 8 images. The image number defines the image
        self.image_num = in_image_num
        self.index = in_index
        tile_dimensions = (60, 80)
        image_path = "..//resources//images//tile_img_{}_tp.png".format(in_image_num)
        self.image =  pg.transform.scale(pg.image.load(image_path),
                                         tile_dimensions).convert_alpha()

