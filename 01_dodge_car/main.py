# Import the necessary libraries
import pygame as pg
from menu_screen import MenuScreen
from game_screen import GameScreen
from pause_screen import PauseScreen

# Initialize Pygame
pg.init()
screen_width, screen_height = 300, 500
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Dodge Car")
clock = pg.time.Clock()

# Screens
menuScreen = MenuScreen()
gameScreen = GameScreen()
pauseScreen = PauseScreen()
screens = {'menu': menuScreen, 'game': gameScreen, 'pause': pauseScreen}
current_screen = screens['menu']


# Function to handle the movement of car
def move_car(in_direction):
    if in_direction == 'left':
        print('left')
    elif in_direction == 'right':
        print('right')


# Main loop
running = True
while running:
    # Handle Pygame Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Handle Key Press Events
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                move_car('left')
            elif event.key == pg.K_d:
                move_car('right')

    current_screen = screens[current_screen.active_screen()]
    current_screen.draw_screen()

    pg.display.flip()
    clock.tick(60)


# Quit Pygame
pg.quit()
