import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

class Button:
    def __init__(self, text, center, in_font):
        self.text = text
        self.surface = in_font.render(text, True, BLACK)
        self.rect = self.surface.get_rect(center=center)
        self.bg_rect = self.rect.inflate(20, 10)

    def draw(self, screen):
        pg.draw.rect(screen, GRAY, self.bg_rect)
        screen.blit(self.surface, self.rect)

    def clicked(self, pos):
        return self.bg_rect.collidepoint(pos)
