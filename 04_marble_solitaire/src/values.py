import pygame as pg

screen_dims = [400, 600]
colors = {'WHITE': (255, 255, 255),
          'RED': (255, 0, 0)}

# Create the pygame clock
game_clock = pg.time.Clock()
fps = 60

# Location of Game Screen Buttons
start_new_rect = pg.Rect(50, 515, 125, 25)
start_quit_rect = pg.Rect(225, 515, 125, 25)
start_settings_circle = (363, 38, 23)

game_pause_circle = (35, 32, 21)
game_settings_circle = (363, 32, 21)

settings_save_rect = pg.Rect(145, 450, 115, 33)
settings_music_rect = pg.Rect(260, 215, 35, 30)

pause_resume_rect = pg.Rect(100, 240, 200, 40)
pause_main_rect = pg.Rect(100, 315, 200, 35)
pause_quit_rect = pg.Rect(100, 380, 200, 35)

over_new_rect = pg.Rect(95, 215, 205, 35)
over_main_rect = pg.Rect(95, 285, 205, 35)
over_quit_rect = pg.Rect(95, 350, 205, 40)

music_on = True
settings_circles = {'red': (109, 332, 27), 'blue': (201, 332, 27), 'green': (291, 332, 27),
                    'yellow': (109, 395, 27), 'white': (201, 395, 27), 'black': (291, 395, 27)}
marble_color = 'blue'

# Game Screen Status
# 0: Game Ongoing     1: Game Lost     2: Game Won
