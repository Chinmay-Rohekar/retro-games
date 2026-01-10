import pygame as pg

# Screen Dimensions
screen_dims = [300, 500]

# Colors
colors = {'RED': (255, 0, 0), 'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255),
          'YELLOW': (255, 255, 0), 'WHITE': (255, 255, 255), 'GRAY': (127, 127, 127),
          'BLACK': (0, 0, 0), 'DARK_GUNMETAL': (58, 58, 58), 'WARM_GOLD': (242, 201, 76),
          'LIGHT_METAL': (74, 74, 74), 'STEEL': (142, 142, 142)}

game_pause_rect = pg.Rect(10, 5, 40, 40)
game_home_rect = pg.Rect(250, 5, 40, 40)

game_clock = pg.time.Clock()
