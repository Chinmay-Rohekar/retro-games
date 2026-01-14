import pygame as pg
from enemy_shell import EnemyShell
from values import enemy_max_health, enemy_shell_speed, enemy_reload_time
from values import explosion_images

class EnemyTank:
    def __init__(self, in_screen, in_pos_x, in_pos_y):
        self.font = pg.font.SysFont(None, 30)
        self.screen = in_screen
        self.pos_x = in_pos_x
        self.pos_y = in_pos_y
        self.health = enemy_max_health
        self.gun_time = 3
        self.shoot_time = 0
        self.tank_image = pg.transform.scale(pg.image.load("../resources/images/tank_red.png"),
                                         (75, 120))
        self.shells = []
        self.fired = True
        self.gun_sound = pg.mixer.Sound("..//resources//music//tank_shot_sound.mp3")
        self.gun_sound.set_volume(1.0)
        self.explosion_sound = pg.mixer.Sound("..//resources//music//tank_explosion_sound.mp3")
        self.explosion_sound.set_volume(1.0)
        self.explode = False
        self.explode_frame = 0

    def set_health(self, in_health):
        self.health = in_health

    def draw_tank(self):
        self.screen.blit(self.tank_image, (self.pos_x * 75, self.pos_y))

        for shell in self.shells[:]:
            shell.pos_y += enemy_shell_speed
            if shell.pos_y > 430:
                self.shells.remove(shell)
            else:
                shell.draw_shell()

        if self.explode and self.explode_frame <= len(explosion_images)*4:
            if self.explode_frame == len(explosion_images)*4:
                self.explode = False
                self.explode_frame = 0

            else:
                self.screen.blit(explosion_images[self.explode_frame//4],
                                 (self.pos_x * 75, self.pos_y))
                self.explode_frame += 1


    def shoot_shell(self, in_gun_time, in_x_pos, in_y_pos):
        self.gun_time = in_gun_time
        if self.gun_time-self.shoot_time >= enemy_reload_time:
            self.shells.append(EnemyShell(self.screen, in_x_pos, in_y_pos))
            self.gun_sound.play()
            self.shoot_time = self.gun_time

    def check_collision(self, in_player_tank):
        tank_image_rect = pg.Rect(self.pos_x * 75, self.pos_y, 75, 60)
        for player_shell in in_player_tank.shells:
            shell_image_rect = pg.Rect((player_shell.pos_x * 75) + 31, player_shell.pos_y, 12, 40)
            if tank_image_rect.colliderect(shell_image_rect):
                self.health -= 1
                self.health = max(self.health, 0)
                in_player_tank.shells.remove(player_shell)
                in_player_tank.increase_score()
                self.explosion_sound.play()

                self.explode = True
                self.explode_frame = 0

    def draw_explosion(self):
        pass

