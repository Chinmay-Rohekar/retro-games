# Import the necessary libraries
import pygame as pg
from values import screen_dims
from start_screen import StartScreen
from game_screen import GameScreen

# Initialize Pygame
pg.init()
screen_width, screen_height = 300, 500
screen = pg.display.set_mode((screen_dims[0], screen_dims[1]))
pg.display.set_caption("Dodge Car")
# Timer Variables
clock = pg.time.Clock()
fps = 60
# Music Variables
pg.mixer.init()

# Screens
start_screen = StartScreen(screen)
game_screen = GameScreen(screen)
screens = {'start': start_screen, 'game': game_screen}
current_screen = screens['start']
current_screen.start_music()

# Important Functions
def change_screen(in_close_screen, in_open_screen):
    if in_close_screen is not None:
        in_close_screen.stop_music()
    in_open_screen.start_music()

# Main Loop
running = True
while running:
    clock.tick(fps)
    # Handle Pygame Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Handle Mouse Clicks on Buttons
    mouse_buttons = pg.mouse.get_pressed()
    if mouse_buttons[0]:
        mouse_x, mouse_y = pg.mouse.get_pos()
        if current_screen == start_screen:
            if start_screen.button_start.button_rect.collidepoint(mouse_x, mouse_y):
                current_screen = screens['game']
                change_screen(start_screen, screens['game'])
            elif start_screen.button_quit.button_rect.collidepoint(mouse_x, mouse_y):
                running = False

    # Checking Mouse Position
    mouse_pos = pg.mouse.get_pos()
    if current_screen == start_screen:
        for button in current_screen.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.hover_state = True  # hover color
            else:
                button.hover_state = False

    current_screen.draw_screen()
    pg.display.flip()

# Quit Pygame
pg.quit()
