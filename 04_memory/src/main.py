# Import the necessary libraries
import pygame as pg
from menu_screen import MenuScreen
from colors import colors, screen_dims


# Initialize Pygame
pg.init()
screen_width, screen_height = screen_dims['width'], screen_dims['height']
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Memory Tiles")
# Timer Variables
clock = pg.time.Clock()

player_score = 0

# Screens
menuScreen = MenuScreen(screen)
# gameScreen = GameScreen(screen)
# pauseScreen = PauseScreen(screen)
# scoreScreen = ScoreScreen(screen)
screens = {'menu': menuScreen}
# screens = {'menu': menuScreen, 'game': gameScreen, 'pause': pauseScreen, 'score': scoreScreen}
current_screen = screens['menu']

# Main loop
running = True
while running:
    # Handle Pygame Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(colors['WHITE'])
    current_screen.draw_screen()

    pg.display.flip()

# Quit Pygame
pg.quit()
