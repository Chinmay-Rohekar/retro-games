import pygame as pg

screen_dims = (400, 600)
colors = {'WHITE': (255, 255, 255),
          'BLACK': (0, 0, 0) }

game_clock = pg.time.Clock()
fps = 60
elapsed_ms = 0
elapsed_sec = 0

# Positions of the buttons
# Start Screen
start_new_rect = pg.Rect(98, 256, 203, 46)
start_quit_rect = pg.Rect(98, 320, 203, 46)
# Game Screen
game_pause_circle = (35, 35, 21)
game_settings_circle = (365, 33, 21)
# Pause Screen
pause_resume_rect = pg.Rect(97, 187, 207, 39)
pause_main_rect = pg.Rect(97, 261, 207, 39)
pause_quit_rect = pg.Rect(97, 335, 207, 39)
