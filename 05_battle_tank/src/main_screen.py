import pygame as pg
import values

class MainScreen:
    def __init__(self, in_screen):
        self.screen = in_screen


        # Load the necessary image
        image_path = '..//resources//first_screen_image.png'  # Replace with the path to your image
        self.background_image = pg.image.load(image_path)
        self.background_image = pg.transform.scale(self.background_image,
                                                   (values.screen_width, values.screen_height))

    def draw_screen(self):
        # First clear the screen
        self.screen.fill((255, 255, 255))
        # Draw the Background Image
        self.screen.blit(self.background_image, (0, 0))
        # Draw the start game button
        
