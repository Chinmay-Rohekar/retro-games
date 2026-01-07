# Import the necessary libraries
import pygame as pg
import values
from main_screen import MainScreen

# Initialize Pygame
pg.init()
# Create the Screen
screen = pg.display.set_mode((values.screen_width, values.screen_height))
pg.display.set_caption('Battle Tank')
# Create the Clock
clock = pg.time.Clock()
FPS = 30
# Define the various screens
mainScreen = MainScreen(screen)
screens = {'main': mainScreen}
current_screen = screens['main']

# Declare the various functions

# Create the main Game loop
running = True
while running:
    # Handle the various events
    for event in pg.event.get():
        # Window Quit Event
        if event.type == pg.QUIT:
            running = False

    # Update the Screen
    current_screen.draw_screen()
    pg.display.flip()
    clock.tick(FPS)

# Quit Pygame
pg.quit()
