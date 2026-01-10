import pygame as pg
from values import colors
from shell import Shell

class Tank:
    def __init__(self, in_screen, in_pos_x, in_pos_y):
        self.font = pg.font.SysFont(None, 30)
        self.screen = in_screen
        self.pos_x = in_pos_x
        self.pos_y = in_pos_y
        self.health = 4
        self.gun_time = 3
        self.shoot_time = 0
        self.tank_image = pg.transform.scale(pg.image.load("../resources/images/tank_blue.png"),
                                        (75, 120))
        self.shells = []
        self.fired = True
        self.gun_time_text = self.font.render(str(self.gun_time), True, colors['WHITE'])
        self.gun_time_rect = self.gun_time_text.get_rect(center=(275, 480))

    def set_health(self, in_health):
        self.health = in_health

    def draw_tank(self):
        self.screen.blit(self.tank_image, (self.pos_x * 75, self.pos_y))
        pg.draw.rect(self.screen, colors['BLACK'], rect=(50, 475, 200, 10), border_radius=5)
        if self.health > 0:
            pg.draw.rect(self.screen, colors['BLUE'], rect=(50, 475, self.health*50, 10),
                         border_radius=5)
        pg.draw.circle(self.screen, colors['BLUE'], (275, 480), 15)
        self.screen.blit(self.gun_time_text, self.gun_time_rect)

        for shell in self.shells[:]:
            shell.pos_y -= 1
            if shell.pos_y < 50:
                self.shells.remove(shell)
            else:
                shell.draw_shell()

    def shoot_shell(self, in_gun_time, in_x_pos, in_y_pos):
        self.gun_time = in_gun_time
        if self.gun_time-self.shoot_time >= 1.5:
            self.shells.append(Shell(self.screen, in_x_pos, in_y_pos))
            self.shoot_time = self.gun_time

    def check_collision(self, in_enemy_tank):
        tank_image_rect = pg.Rect(self.pos_x * 75, self.pos_y+30, 75, 90)
        for enemy_shell in in_enemy_tank.shells:
            shell_image_rect = pg.Rect((enemy_shell.pos_x*75) + 31, enemy_shell.pos_y, 12, 40)
            if tank_image_rect.colliderect(shell_image_rect):
                self.health -= 1
                self.health = max(self.health, 0)
                in_enemy_tank.shells.remove(enemy_shell)
                break

