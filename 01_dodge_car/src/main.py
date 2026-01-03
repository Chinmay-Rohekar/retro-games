# Import the necessary libraries
import pygame as pg
from menu_screen import MenuScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from score_screen import ScoreScreen
from car import Car
from random import choice

# Initialize Pygame
pg.init()
screen_width, screen_height = 300, 500
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Dodge Car")
# Timer Variables
clock = pg.time.Clock()
timer = 0
interval = 1  # seconds

player_score = 0

# Screens
menuScreen = MenuScreen(screen)
gameScreen = GameScreen(screen)
pauseScreen = PauseScreen(screen)
scoreScreen = ScoreScreen(screen)
screens = {'menu': menuScreen, 'game': gameScreen, 'pause': pauseScreen, 'score': scoreScreen}
current_screen = screens['menu']

player_car = Car('player', [10, 400])
enemy_cars = []

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)


# Function to randomly generate an enemy car
def generate_car():
    enemy_car = Car('enemy', [choice([10, 110, 210]), -20])
    enemy_car.speed_y = 5
    enemy_cars.append(enemy_car)


# Main loop
running = True
while running:
    # Handling Timer
    dt = clock.tick(60) / 1000  # seconds
    timer += dt
    # Handle Pygame Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Handle Key Press Events
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                player_car.move_x('a')
            elif event.key == pg.K_d:
                player_car.move_x('d')
            elif event.key == pg.K_g:
                generate_car()
        # Handle Mouse Clicks on Buttons
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if current_screen == menuScreen:
                if menuScreen.button1.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['game']
                elif menuScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    running = False
            elif current_screen == gameScreen:
                if gameScreen.button1.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['menu']
                elif gameScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['pause']
            elif current_screen == pauseScreen:
                if pauseScreen.button1.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['menu']
                elif pauseScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['game']
                elif pauseScreen.button3.rect_button.collidepoint(mouse_x, mouse_y):
                    running = False
            elif current_screen == scoreScreen:
                if scoreScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['menu']
                elif scoreScreen.button2.rect_button.collidepoint(mouse_x, mouse_y):
                    current_screen = screens['game']
                elif scoreScreen.button3.rect_button.collidepoint(mouse_x, mouse_y):
                    running = False


    screen.fill(WHITE)
    current_screen.draw_screen()

    if current_screen == gameScreen:
        if timer >= interval:
            generate_car()
            timer = 0
        current_screen.draw_score(player_score)
        for enemy_car in enemy_cars:
            enemy_car.move_y()
            enemy_car.draw_car(screen)

            if enemy_car.get_bounding_rect().colliderect(player_car.get_bounding_rect()):
                current_screen = screens['score']
                current_screen.fin_score = player_score
            if enemy_car.pos[1] > 600:
                enemy_cars.remove(enemy_car)
                player_score += 1

        player_car.draw_car(screen)

    pg.display.flip()


# Quit Pygame
pg.quit()
