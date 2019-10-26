import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, settings, screen):
        super(Ball, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.ball_width,
                                settings.ball_height)
        self.color = settings.ball_color
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 100

        self.settings = settings

        self.center = float(self.rect.centerx)

        self.speed_factor_y = settings.ball_speed_factor_y
        self.speed_factor_x = settings.ball_speed_factor_x

        self.moving_up = False
        self.moving_down = True
        self.moving_right = False
        self.moving_left = False

    def update_ball(self):
        if self.moving_up:
            if self.rect.top <= self.screen_rect.top:
                self.moving_up = False
                self.moving_down = True
            else:
                self.rect.y -= self.speed_factor_y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed_factor_y
        if self.moving_right:
            if self.rect.right >= self.screen_rect.right:
                self.moving_right = False
                self.moving_left = True
            else:
                self.rect.centerx += self.speed_factor_x
        if self.moving_left:
            if self.rect.left <= self.screen_rect.left:
                self.moving_left = False
                self.moving_right = True
            else:
                self.rect.centerx -= self.speed_factor_x

    def reset_ball(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 100

        self.moving_up = False
        self.moving_down = True
        self.moving_right = False
        self.moving_left = False

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
