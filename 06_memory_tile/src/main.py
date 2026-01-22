# Import the necessary libraries
import pygame as pg
from values import screen_dims, game_clock, fps
from values import start_new_rect, start_quit_rect, game_pause_circle, game_settings_circle
import values
from start_screen import StartScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from end_screen import EndScreen

# Initialize Pygame
pg.init()
screen = pg.display.set_mode(screen_dims)
pg.display.set_caption("Memory Tile")

# Create all the screens
start_screen = StartScreen(screen)
game_screen = GameScreen(screen)
pause_screen = PauseScreen(screen)
end_screen = EndScreen(screen)
screens = {'start': start_screen, 'game': game_screen, 'pause': pause_screen,
           'end': end_screen}
current_screen = screens['start']


# Function for checking collision with the circle
def collision_circle(in_mouse_pos, in_circle_dims):
    if((in_mouse_pos[0] - in_circle_dims[0])**2 +
       (in_mouse_pos[1] - in_circle_dims[1])**2) <= in_circle_dims[2]**2:
        return True

    return False


# Create the main game loop
running = True
while running:
    # Set the time specifications
    game_clock.tick(fps)
    values.elapsed_ms = pg.time.get_ticks()
    values.elapsed_sec = values.elapsed_ms/1000

    # Handle the various events in the Pygame
    for event in pg.event.get():
        # Handling the Quit Event
        if event.type == pg.QUIT:
            running = False

        # Handling the Mouse Click Events
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            print(mouse_pos)

            # Current Screen is the Start Screen
            if current_screen == screens['start']:
                if start_new_rect.collidepoint(mouse_pos):
                    current_screen = screens['game']
                elif start_quit_rect.collidepoint(mouse_pos):
                    # Quit the Game
                    running = False

            # Current Screen is the Game Screen
            if current_screen == screens['game']:
                if collision_circle(mouse_pos, game_pause_circle):
                    current_screen = screens['pause']

            # Current Screen is the Pause Screen
            if current_screen == screens['pause']:





    # Update and Display the current screen
    current_screen.draw_screen()
    pg.display.flip()

# Quit the Pygame
pg.quit()
