# Import the pygame library
import pygame as pg
from paddle import Paddle

# Variables
screen_width = 300
screen_height = 500
game_paused = True
# Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Function to update the view
def update_view():
    # Fill the entire background with a color
    screen.fill(YELLOW)
    # Draw the Top Bar
    pg.draw.rect(screen, GREEN, (0,0,300,60))
    # Draw the Start/Pause Button
    if game_paused:
        screen.blit(img_pause, rect_pause)
    else:
        screen.blit(img_start, rect_start)
    # Draw the Stop Button
    screen.blit(img_stop, rect_stop)
    # Draw the Score
    text_score = font.render('{} : {}'.format(player.score, opponent.score),
                             True, BLUE)
    rect_score = text_score.get_rect()
    rect_score.center = 150, 33
    screen.blit(text_score, rect_score)
    # Draw the border
    pg.draw.rect(screen, BLACK,(0, 60, 300, 440), 5)
    # Draw the Center Line
    pg.draw.line(screen, BLACK, (0, 280), (300, 280), 5)
    # Draw the Paddles
    player.draw_paddle(screen)                    # Draw the Player's Paddle
    opponent.draw_paddle(screen)                  # Draw the Opponent's Paddle


# Initialize pygame
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
# Create the Clock
clock = pg.time.Clock()
FPS = 30

# Create the two paddles
player = Paddle('player')
opponent = Paddle('opponent')

# Load all the images
img_start = pg.image.load('..//resources//play.png')
img_stop = pg.image.load('..//resources//stop.png')
img_pause = pg.image.load('..//resources//pause.png')
img_start.convert()
img_stop.convert()
img_pause.convert()
rect_start = img_start.get_rect()
rect_stop = img_stop.get_rect()
rect_pause = img_pause.get_rect()
rect_start.center = 40, 30
rect_pause.center = 40, 30
rect_stop.center = 260, 30
font = pg.font.SysFont(None, 60)

# Create the main Game loop
running = True
while running:
    # Handle the various events
    for event in pg.event.get():
        # Window Quit Event
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    # for the player's paddle
    if keys[pg.K_a]:
        player.speed_x = -5
    elif keys[pg.K_d]:
        player.speed_x = 5
    else:
        player.speed_x = 0

    if keys[pg.K_w]:
        player.speed_y = -5
    elif keys[pg.K_s]:
        player.speed_y = 5
    else:
        player.speed_y = 0

    # for the opponent's paddle
    if keys[pg.K_LEFT]:
        opponent.speed_x = -5
    elif keys[pg.K_RIGHT]:
        opponent.speed_x = 5
    else:
        opponent.speed_x = 0

    if keys[pg.K_UP]:
        opponent.speed_y = -5
    elif keys[pg.K_DOWN]:
        opponent.speed_y = 5
    else:
        opponent.speed_y = 0

    # Move the Paddle
    player.move()
    opponent.move()
    # Update the View
    update_view()
    pg.display.flip()
    clock.tick(FPS)

# Quit Pygame
pg.quit()
