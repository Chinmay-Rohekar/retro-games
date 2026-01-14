import pygame as pg
from values import colors, player_max_health, screen_dims, player_shell_speed, player_reload_time
from shell import Shell

class Tank:
    def __init__(self, in_screen, in_pos_x, in_pos_y):
        self.font = pg.font.SysFont(None, 30)
        self.screen = in_screen
        self.pos_x = in_pos_x
        self.pos_y = in_pos_y
        self.health = player_max_health
        self.shoot_time = 0
        self.tank_image = pg.transform.scale(pg.image.load("../resources/images/tank_blue.png"),
                                        (75, 120))
        self.shells = []
        self.fired = True
        self.gun_sound = pg.mixer.Sound("..//resources//music//tank_shot_sound.mp3")
        self.gun_sound.set_volume(1.0)
        self.score = 0
        self.explosion_sound = pg.mixer.Sound("..//resources//music//tank_explosion_sound.mp3")
        self.explosion_sound.set_volume(1.0)
        self.gun_time = 0

    def set_health(self, in_health):
        self.health = in_health

    def draw_tank(self):
        score_text = self.font.render("SCORE: {}".format(self.score), True, colors['WARM_GOLD'])
        score_rect = score_text.get_rect(center=(screen_dims[0] // 2, 25))
        self.screen.blit(score_text, score_rect)
        self.screen.blit(self.tank_image, (self.pos_x * 75, self.pos_y))
        pg.draw.rect(self.screen, colors['BLACK'], rect=(50, 475, 200, 10), border_radius=5)
        if self.health > 0:
            pg.draw.rect(self.screen, colors['BLUE'], rect=(50, 475, self.health*50, 10),
                         border_radius=5)

        for shell in self.shells[:]:
            shell.pos_y -= player_shell_speed
            if shell.pos_y < 50:
                self.shells.remove(shell)
            else:
                shell.draw_shell()

    def shoot_shell(self, in_gun_time, in_x_pos, in_y_pos):
        self.gun_time = in_gun_time
        if self.gun_time-self.shoot_time >= player_reload_time:
            self.gun_sound.play()
            self.shells.append(Shell(self.screen, in_x_pos, in_y_pos))
            self.shoot_time = self.gun_time

    def check_collision_tank(self, in_enemy_tank):
        tank_image_rect = pg.Rect(self.pos_x * 75, self.pos_y+30, 75, 90)
        for enemy_shell in in_enemy_tank.shells:
            shell_image_rect = pg.Rect((enemy_shell.pos_x*75) + 31, enemy_shell.pos_y, 12, 40)
            if tank_image_rect.colliderect(shell_image_rect):
                self.health -= 1
                self.health = max(self.health, 0)
                in_enemy_tank.shells.remove(enemy_shell)
                self.explosion_sound.play()

    def check_collision_shell(self, in_enemy_tank):
        for enemy_shell in in_enemy_tank.shells:
            for player_shell in self.shells[:]:
                shell_image_rect = pg.Rect((enemy_shell.pos_x*75) + 31, enemy_shell.pos_y, 12, 40)
                player_shell_rect = pg.Rect((player_shell.pos_x*75) + 31, player_shell.pos_y, 12, 40)
                if shell_image_rect.colliderect(player_shell_rect):
                    in_enemy_tank.shells.remove(enemy_shell)
                    self.shells.remove(player_shell)


    def increase_score(self):
        self.score += 1

