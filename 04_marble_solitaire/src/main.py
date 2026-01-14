# Import the necessary libraries
import pygame as pg
from values import screen_dims, game_clock, fps
from start_screen import StartScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from over_screen import OverScreen


# Initialize Pygame
pg.init()
screen = pg.display.set_mode((screen_dims[0], screen_dims[1]))
pg.display.set_caption("Marble Solitaire")
# Initialize Music Mixer
pg.mixer.init()

# Create all the screens
start_screen = StartScreen(screen)
game_screen = GameScreen(screen)
pause_screen = PauseScreen(screen)
over_screen = OverScreen(screen)

# Create the main game loop
running = True
while running:
    game_clock.tick(fps)
    # Get the elapsed time
    elapsed_ms = pg.time.get_ticks()
    elapsed_sec = elapsed_ms/1000.0

