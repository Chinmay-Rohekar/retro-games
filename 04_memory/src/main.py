# Import the necessary libraries
import pygame as pg
from menu_screen import MenuScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from colors import colors, screen_dims


# Initialize Pygame
pg.init()
screen_width, screen_height = screen_dims['width'], screen_dims['height']
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Memory Tiles")
# Timer Variables
clock = pg.time.Clock()
# Game Variables
game_on = False
player_score = 0

# Screens
menuScreen = MenuScreen(screen)
gameScreen = GameScreen(screen)
pauseScreen = PauseScreen(screen)
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

        if event.type == pg.MOUSEBUTTONDOWN:
            # Handle Button Clicks for Various Screens
            mouse_x, mouse_y = pg.mouse.get_pos()
            if current_screen == menuScreen:
                if menuScreen.button1.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['game']     # Start Game
                elif menuScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    running = False     # Quit Game
            elif current_screen == gameScreen:
                if gameScreen.button1.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['pause']     # Pause Game
                elif gameScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    running = False     # Quit Game

    screen.fill(colors['WHITE'])
    current_screen.draw_screen()

    pg.display.flip()

# Quit Pygame
pg.quit()
