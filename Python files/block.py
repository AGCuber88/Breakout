import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, settings, screen):
        super(Block, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.block_width,
                                settings.block_height)

        self.color = settings.block_color

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw_block(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
