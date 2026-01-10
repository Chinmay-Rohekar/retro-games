# Import the necessary libraries
import pygame as pg
from values import screen_dims, game_pause_rect, game_home_rect, game_clock
from start_screen import StartScreen
from game_screen import GameScreen
from pause_screen import PauseScreen
from tank import Tank
from enemy_tank import EnemyTank

# Initialize Pygame
pg.init()
screen = pg.display.set_mode((screen_dims[0], screen_dims[1]))
pg.display.set_caption("Battle Tank")
# Timer Variables
fps = 60
# Music Variables
pg.mixer.init()

# Screens
start_screen = StartScreen(screen)
game_screen = GameScreen(screen)
pause_screen = PauseScreen(screen)
screens = {'start': start_screen, 'game': game_screen, 'pause': pause_screen}
current_screen = screens['start']
current_screen.start_music()

# Create the Player Tank
player_tank = Tank(screen, 0, 350)
enemy_tank = EnemyTank(screen, 0, 50)

# Important Functions
def change_screen(in_close_screen, in_open_screen):
    global current_screen
    current_screen = in_open_screen
    if in_close_screen is not None:
        in_close_screen.stop_music()
    in_open_screen.start_music()

# Main Loop
running = True
while running:
    # Setting the fps and the time
    game_clock.tick(fps)
    elapsed_ms = pg.time.get_ticks()
    elapsed_sec = elapsed_ms / 1000
    # Handle Pygame Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Handle Key Press Events
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_tank.pos_x -= 1
                player_tank.pos_x = max(0, min(player_tank.pos_x, 3))
            elif event.key == pg.K_RIGHT:
                player_tank.pos_x += 1
                player_tank.pos_x = max(0, min(player_tank.pos_x, 3))
            elif event.key == pg.K_SPACE:
                player_tank.shoot_shell(elapsed_sec, player_tank.pos_x, 320)
            elif event.key == pg.K_b:
                enemy_tank.shoot_shell(elapsed_sec, enemy_tank.pos_x, 160)

    # Handle Mouse Clicks on Buttons
    mouse_buttons = pg.mouse.get_pressed()
    if mouse_buttons[0]:
        mouse_x, mouse_y = pg.mouse.get_pos()
        # Checking Mouse Position for Button CLicks
        if current_screen == start_screen:
            if start_screen.button_start_rect.collidepoint(mouse_x, mouse_y):
                change_screen(screens['start'], screens['game'])
            elif start_screen.button_quit_rect.collidepoint(mouse_x, mouse_y):
                running = False

        if current_screen == game_screen:
            if game_pause_rect.collidepoint(mouse_x, mouse_y):
                change_screen(screens['game'], screens['pause'])
            elif game_home_rect.collidepoint(mouse_x, mouse_y):
                change_screen(screens['game'], screens['start'])

        if current_screen == pause_screen:
            if pause_screen.button_resume_rect.collidepoint(mouse_x, mouse_y):
                change_screen(screens['pause'], screens['game'])
            elif pause_screen.button_main_rect.collidepoint(mouse_x, mouse_y):
                change_screen(screens['pause'], screens['start'])
            elif pause_screen.button_quit_rect.collidepoint(mouse_x, mouse_y):
                running = False


    # Checking Mouse Position for Hover
    mouse_pos = pg.mouse.get_pos()
    if current_screen == start_screen:
        for button in current_screen.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.hover_state = True  # hover color
            else:
                button.hover_state = False
    if current_screen == pause_screen:
        for button in pause_screen.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.hover_state = True  # hover color
            else:
                button.hover_state = False

    current_screen.draw_screen()

    # Drawing the Player Tank
    if current_screen == game_screen:
        player_tank.draw_tank()
        enemy_tank.draw_tank()
        player_tank.check_collision(enemy_tank)
        # enemy_tank.check_collision(player_tank.shells)

    pg.display.flip()

# Quit Pygame
pg.quit()
