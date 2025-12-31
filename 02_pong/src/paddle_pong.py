# Import the pygame library
import pygame as pg
from paddle import Paddle
from ball import Ball
from random import choice

# Variables
screen_width = 300
screen_height = 500
game_paused = False
game_over = False
winner_text = ""

# Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Function to Reset Turn
def turn_reset():
    disc.reset_ball()

# Function to update the score
def update_score(in_winner):
    global game_paused, game_over, winner_text
    if in_winner == 'player':
        player.score += 1
        if player.score == 10:
            winner_text = "PLAYER WINS"
            game_over = True
            game_paused = True

    elif in_winner == 'opponent':
        opponent.score += 1
        if opponent.score == 10:
            winner_text = "OPPONENT WINS"
            game_over = True
            game_paused = True


# Function to Draw the Game Over
def draw_game_over():
    overlay = pg.Surface((300, 500))
    overlay.set_alpha(180)  # transparency
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))

    text_game_over = font.render("GAME OVER", True, WHITE)
    rect_game_over = text_game_over.get_rect(center=(150, 220))
    screen.blit(text_game_over, rect_game_over)

    text_winner = font.render(winner_text, True, YELLOW)
    rect_winner = text_winner.get_rect(center=(150, 280))
    screen.blit(text_winner, rect_winner)

    text_restart = pg.font.SysFont(None, 36).render(
        "Click START to play again", True, WHITE
    )
    rect_restart = text_restart.get_rect(center=(150, 330))
    screen.blit(text_restart, rect_restart)


# Function to update the view
def update_view():
    # Fill the entire background with a color
    screen.fill(YELLOW)
    # Draw the Top Bar
    pg.draw.rect(screen, GREEN, (0,0,300,60))
    # Draw the Start/Pause Button
    if game_paused:
        screen.blit(img_start, rect_start)
    else:
        screen.blit(img_pause, rect_pause)
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
    # Write the names of the players
    screen.blit(text_player, rect_player)
    screen.blit(text_opponent, rect_opponent)
    # Draw the Paddles
    player.draw_paddle(screen)                    # Draw the Player's Paddle
    opponent.draw_paddle(screen)                  # Draw the Opponent's Paddle
    disc.draw_ball(screen)

    if game_over:
        draw_game_over()


# Initialize pygame
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
# Create the Clock
clock = pg.time.Clock()
FPS = 30

# Create the two paddles
player = Paddle('player')
opponent = Paddle('opponent')
disc = Ball()
# Randomly set the disc's speed
disc.speed_x = choice([5, -5])
disc.speed_y = choice([5, -5])

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

text_player = font.render('Player', True, BLUE)
rect_player = text_player.get_rect()
rect_player.center = 150, 390
text_opponent = font.render('Opponent', True, RED)
rect_opponent = text_opponent.get_rect()
rect_opponent.center = 150, 170

# Create the main Game loop
running = True
while running:
    # Handle the various events
    for event in pg.event.get():
        # Window Quit Event
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_pos = event.pos
            if rect_start.collidepoint(event.pos):
                game_paused = not game_paused
            if rect_start.collidepoint(event.pos):
                if game_over:
                    player.score = 0
                    opponent.score = 0
                    game_over = False
                    disc.reset_ball()
                game_paused = False

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

    # Move the Paddles and Disc
    if not game_paused:
        player.move()
        opponent.move()
        result = disc.move()
        if result is not None:
            update_score(result)

    # Detecting Collision
    ball_rect = disc.get_rect()
    player_rect = player.get_rect()
    opponent_rect = opponent.get_rect()
    if ball_rect.colliderect(player_rect) or ball_rect.colliderect(opponent_rect):
        disc.speed_y *= -1

    # Update the View
    update_view()
    pg.display.flip()
    clock.tick(FPS)

# Quit Pygame
pg.quit()
