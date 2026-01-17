# Import the necessary libraries
import pygame as pg
from values import screen_dims, game_clock, fps, start_settings_circle, settings_save_rect
from values import start_new_rect, start_quit_rect, game_pause_circle, game_settings_circle
from values import pause_resume_rect, pause_main_rect, pause_quit_rect, settings_music_rect
from values import over_new_rect, over_main_rect, over_quit_rect, settings_circles
import values
from start_screen import StartScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from settings_screen import SettingsScreen
from over_screen import OverScreen

# Initialize Pygame
pg.init()
screen = pg.display.set_mode((screen_dims[0], screen_dims[1]))
pg.display.set_caption("Marble Solitaire")
# music_tag: Initialize Music Mixer
pg.mixer.init()

# Create all the screens
start_screen = StartScreen(screen)
game_screen = GameScreen(screen)
pause_screen = PauseScreen(screen)
settings_screen = SettingsScreen(screen)
over_screen = OverScreen(screen)
screens = {'start': start_screen, 'game': game_screen, 'pause': pause_screen, 'settings': settings_screen,
           'over': over_screen}
current_screen = screens['start']
game_state = False

# Define all the necessary Functions
# Function to change the screens
def change_screen(in_prev_screen, in_new_screen):
    global current_screen
    if in_prev_screen is not None:
        screens[in_prev_screen].stop_music()        # music_tag: stop the music of the previous screen
    # if music_on:                                  # music_tag: check if the music is on or off
    screens[in_new_screen].start_music()            # music_tag: start the new music of the new screen
    current_screen = screens[in_new_screen]

# Function to start a new game
def start_new_game():
    global game_state
    game_state = True
    game_screen.reset_board()


change_screen(None, 'start')
# Create the main game loop
running = True

while running:
    game_clock.tick(fps)
    # Get the elapsed time
    elapsed_ms = pg.time.get_ticks()
    elapsed_sec = elapsed_ms/1000.0

    # Handling the various events in the game
    for event in pg.event.get():
        # Handle the Quitting of the game
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            # Handling the mouse events
            mouse_pos = pg.mouse.get_pos()
            print("Mouse pressed")
            print(mouse_pos)

            if current_screen == screens['start']:
                if start_new_rect.collidepoint(mouse_pos):
                    # Start a New Game
                    # Change Screen from start_screen to game_screen
                    start_new_game()
                    change_screen('start', 'game')
                elif start_quit_rect.collidepoint(mouse_pos):
                    # Quit the Game
                    running = False
                elif (((mouse_pos[0] - start_settings_circle[0]) ** 2 + (mouse_pos[1] - start_settings_circle[1]) ** 2)
                        <= start_settings_circle[2] ** 2):
                    change_screen('start', 'settings')

            elif current_screen == screens['game']:
                if(((mouse_pos[0]-game_pause_circle[0])**2 + (mouse_pos[1]-game_pause_circle[1])**2)
                        <= game_pause_circle[2]**2):
                    change_screen('game', 'pause')
                elif (((mouse_pos[0] - game_settings_circle[0]) ** 2 + (mouse_pos[1] - game_settings_circle[1]) ** 2)
                        <= game_settings_circle[2] ** 2):
                    change_screen('game', 'settings')
                else:
                    # Handle all the mouse clicks on the board
                    game_screen.handle_mouse_clicks(mouse_pos)

                if game_screen.game_over == 1:
                    # Game has been lost
                    game_state = False
                    over_screen.win = False
                    change_screen('game', 'over')

                elif game_screen.game_over == 2:
                    # Game has been won
                    game_state = False
                    over_screen.win = True
                    change_screen('game', 'over')

            elif current_screen == screens['settings']:
                if settings_save_rect.collidepoint(mouse_pos):
                    if game_state:
                        change_screen('settings', 'game')
                    else:
                        change_screen('settings', 'start')
                elif settings_music_rect.collidepoint(mouse_pos):
                    values.music_on = not values.music_on             # music_tag: Swap the music state
                    print("Main: ", values.music_on)
                    if values.music_on:                        # Play the Music state
                        current_screen.start_music()
                    else:
                        current_screen.stop_music()

                for key, value in settings_circles.items():
                    if (((mouse_pos[0] - value[0]) ** 2 + (mouse_pos[1] - value[1]) ** 2)
                            <= value[2] ** 2):
                        game_screen.change_marble_color(key)

            elif current_screen == screens['pause']:
                if pause_resume_rect.collidepoint(mouse_pos):
                    # Change Screen from pause_screen to game_screen
                    game_state = True
                    change_screen('pause', 'game')
                elif pause_main_rect.collidepoint(mouse_pos):
                    # Change Screen from pause_screen to start_screen
                    game_state = False
                    change_screen('pause', 'start')
                elif pause_quit_rect.collidepoint(mouse_pos):
                    # Quit the Game
                    running = False

            elif current_screen == screens['over']:
                if over_new_rect.collidepoint(mouse_pos):
                    # Change Screen from over_screen to start_screen
                    game_state = True
                    start_new_game()
                    change_screen('over', 'game')
                elif over_main_rect.collidepoint(mouse_pos):
                    # Change Screen from over_screen to start_screen
                    change_screen('over', 'start')
                elif over_quit_rect.collidepoint(mouse_pos):
                    # Quit the Game
                    running = False


    # Update the Screen
    current_screen.draw_screen()
    pg.display.flip()

# Quit Pygame
pg.quit()
