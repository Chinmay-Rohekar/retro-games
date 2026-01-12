import pygame as pg
from values import colors
from enemy_shell import EnemyShell

class EnemyTank:
    def __init__(self, in_screen, in_pos_x, in_pos_y):
        self.font = pg.font.SysFont(None, 30)
        self.screen = in_screen
        self.pos_x = in_pos_x
        self.pos_y = in_pos_y
        self.health = 5
        self.gun_time = 3
        self.shoot_time = 0
        self.tank_image = pg.transform.scale(pg.image.load("../resources/images/tank_red.png"),
                                         (75, 120))
        self.shells = []
        self.fired = True

    def set_health(self, in_health):
        self.health = in_health

    def draw_tank(self):
        self.screen.blit(self.tank_image, (self.pos_x * 75, self.pos_y))

        for shell in self.shells[:]:
            shell.pos_y += 1
            if shell.pos_y > 430:
                self.shells.remove(shell)
            else:
                shell.draw_shell()

    def shoot_shell(self, in_gun_time, in_x_pos, in_y_pos):
        self.gun_time = in_gun_time
        if self.gun_time-self.shoot_time >= 1.5:
            self.shells.append(EnemyShell(self.screen, in_x_pos, in_y_pos))
            self.shoot_time = self.gun_time

    def check_collision(self, in_player_tank):
        tank_image_rect = pg.Rect(self.pos_x * 75, self.pos_y, 75, 60)
        for player_shell in in_player_tank.shells:
            shell_image_rect = pg.Rect((player_shell.pos_x * 75) + 31, player_shell.pos_y, 12, 40)
            if tank_image_rect.colliderect(shell_image_rect):
                self.health -= 1
                self.health = max(self.health, 0)
                in_player_tank.shells.remove(player_shell)
                break

