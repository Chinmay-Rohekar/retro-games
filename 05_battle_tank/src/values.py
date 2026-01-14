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

player_max_health = 4
enemy_max_health = 1
player_shell_speed = 3
enemy_shell_speed = 2
player_reload_time = 0.5
enemy_reload_time = 1

explosion_images = []


def add_explosion_images():
    for count in range(8):
        image = pg.transform.scale(pg.image.load(f"..//resources//images//exp_0{count}.png"),
                                   (75, 75)).convert_alpha()
        explosion_images.append(image)

