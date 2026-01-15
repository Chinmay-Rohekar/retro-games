# Import the necessary libraries
import pygame as pg
from values import screen_dims, game_clock, fps, start_settings_circle, settings_return_rect
from values import start_new_rect, start_quit_rect, game_pause_circle, game_settings_circle
from values import pause_resume_rect, pause_main_rect, pause_quit_rect, music_on, settings_music_rect
from start_screen import StartScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from settings_screen import SettingsScreen
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
settings_screen = SettingsScreen(screen)
over_screen = OverScreen(screen)
screens = {'start': start_screen, 'game': game_screen, 'pause': pause_screen, 'settings': settings_screen,
           'over': over_screen}
current_screen = screens['start']
game_state = True

# Define all the necessary Functions
# Function to change the screens
def change_screen(in_prev_screen, in_new_screen):
    global current_screen
    if in_prev_screen is not None:
        screens[in_prev_screen].stop_music()
    screens[in_new_screen].start_music()
    current_screen = screens[in_new_screen]

# Function to start a new game
def start_new_game():
    global game_state
    game_state = True


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
                    # Change Screen from start_screen to game_screen
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

            elif current_screen == screens['settings']:
                if settings_return_rect.collidepoint(mouse_pos):
                    if game_state:
                        change_screen('settings', 'game')
                    else:
                        change_screen('settings', 'start')
                elif settings_music_rect.collidepoint(mouse_pos):
                    print(music_on)
                    music_on = not music_on

            elif current_screen == screens['pause']:
                if pause_resume_rect.collidepoint(mouse_pos):
                    # Change Screen from start_screen to game_screen
                    change_screen('pause', 'game')
                elif pause_main_rect.collidepoint(mouse_pos):
                    # Change Screen from start_screen to game_screen
                    change_screen('pause', 'start')
                elif pause_quit_rect.collidepoint(mouse_pos):
                    # Quit the Game
                    running = False


    # Update the Screen
    current_screen.draw_screen()
    pg.display.flip()

# Quit Pygame
pg.quit()
