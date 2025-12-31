import pygame as pg
from menu_screen import MenuScreen, MENU, SETTINGS, GAME
from settings_screen import SettingsScreen, QUIT
from game_screen import GameScreen

pg.init()
font = pg.font.SysFont(None, 36)
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Multi-Screen Example")
clock = pg.time.Clock()

# Initialize screens
screens = {
    MENU: MenuScreen(font),
    SETTINGS: SettingsScreen(font),
    GAME: GameScreen(font),
}

current_screen = screens[MENU]

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        result = current_screen.handle_event(event)
        if result == QUIT:
            running = False
        elif result:
            current_screen = screens[result]

    current_screen.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()
