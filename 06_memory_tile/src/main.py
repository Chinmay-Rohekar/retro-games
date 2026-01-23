# Import the necessary libraries
import pygame as pg
from values import screen_dims, game_clock, fps
from values import start_new_rect, start_quit_rect, game_pause_circle, game_music_circle
from values import pause_resume_rect, pause_start_rect, pause_quit_rect, start_music_circle
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

# Initialize and Play the music
pg.mixer.init()
pg.mixer.music.load("..//resources//music//back_music.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.7)

playing_music = True


# Function for checking collision with the circle
def collision_circle(in_mouse_pos, in_circle_dims):
    if((in_mouse_pos[0] - in_circle_dims[0])**2 +
       (in_mouse_pos[1] - in_circle_dims[1])**2) <= in_circle_dims[2]**2:
        return True

    return False

# Function to pause and unpause the music
def play_pause_music():
    global playing_music
    playing_music = not playing_music
    if playing_music:
        pg.mixer.music.unpause()
    else:
        pg.mixer.music.pause()


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
                elif collision_circle(mouse_pos, start_music_circle):
                    play_pause_music()


            # Current Screen is the Game Screen
            elif current_screen == screens['game']:
                if collision_circle(mouse_pos, game_pause_circle):
                    current_screen = screens['pause']
                elif collision_circle(mouse_pos, game_music_circle):
                    play_pause_music()

                # Analyze Clicks on Tiles
                current_screen.check_tile_collision(mouse_pos)


            # Current Screen is the Pause Screen
            elif current_screen == screens['pause']:
                if pause_resume_rect.collidepoint(mouse_pos):
                    # Open the Game Screen to resume the Game
                    current_screen = screens['game']
                elif pause_start_rect.collidepoint(mouse_pos):
                    # Open the start screen
                    current_screen = screens['start']
                elif pause_quit_rect.collidepoint(mouse_pos):
                    # Quit the Game
                    running = False


    # Update and Display the current screen
    current_screen.draw_screen()
    pg.display.flip()

# Quit the Pygame
pg.quit()
