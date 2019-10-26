import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, settings, screen):
        super(Paddle, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.paddle_width,
                                settings.paddle_height)
        self.color = settings.paddle_color
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.settings = settings

        self.center = float(self.rect.centerx)

        self.speed_factor = settings.paddle_speed_factor

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed_factor

    def center_paddle(self):
        self.rect.centerx = self.screen_rect.centerx

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
