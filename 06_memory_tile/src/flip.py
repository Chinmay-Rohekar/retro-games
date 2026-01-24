import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load images
front_img = pygame.image.load("../resources/images/tile_img_0_tp.png").convert_alpha()
back_img = pygame.image.load("../resources/images/tile_back.png").convert_alpha()

CARD_W, CARD_H = front_img.get_size()
card_pos = (WIDTH // 2, HEIGHT // 2)

# Animation state
flip = False
show_front = True
scale = 1.0
flip_speed = 0.08

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flip = True

    if flip:
        scale -= flip_speed
        if scale <= 0:
            scale = 0
            show_front = not show_front
            flip_speed *= -1
        if scale >= 1:
            scale = 1
            flip_speed *= -1
            flip = False

    img = front_img if show_front else back_img

    # Scale width only (fake 3D)
    scaled_width = max(1, int(CARD_W * scale))
    scaled_img = pygame.transform.scale(img, (scaled_width, CARD_H))

    # Keep centered
    rect = scaled_img.get_rect(center=card_pos)

    screen.fill((30, 30, 30))
    screen.blit(scaled_img, rect)
    pygame.display.flip()

pygame.quit()
