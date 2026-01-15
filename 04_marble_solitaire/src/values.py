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

settings_return_rect = pg.Rect(145, 450, 115, 33)
settings_music_rect = pg.Rect(265, 220, 25, 20)

pause_resume_rect = pg.Rect(100, 240, 200, 40)
pause_main_rect = pg.Rect(100, 315, 200, 35)
pause_quit_rect = pg.Rect(100, 380, 200, 35)

music_on = True
marble_color = 'BLUE'
