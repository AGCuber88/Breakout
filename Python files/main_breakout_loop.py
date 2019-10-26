import pygame
from pygame.sprite import Group

import game_functions as gf
from ball import Ball
from button import Button
from game_stats import GameStats
from paddle import Paddle
from scoreboard import Scoreboard
from settings import Settings


def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Breakout")
    stats = GameStats(settings)

    global bg_image
    bg_image = pygame.image.load('bg_image.png').convert()

    paddle = Paddle(settings, screen)
    blocks = Group()
    ball = Ball(settings, screen)
    play_button = Button(settings, screen, "Play")
    sb = Scoreboard(settings, screen, stats)

    gf.create_section(settings, screen, paddle, blocks)

    while True:

        gf.check_events(paddle, settings, screen, stats, play_button, ball, blocks, sb)
        if stats.game_active:
            paddle.update()
            gf.ball_update(screen, paddle, ball, settings, blocks, stats, sb)
            gf.check_game_loss(ball, screen, stats, settings, paddle, blocks, sb)

        update_screen(screen, settings, paddle, blocks, stats, play_button, ball, sb)


def update_screen(screen, settings, paddle, blocks, stats, play_button, ball, sb):
    screen.blit(bg_image, (0, 0))

    paddle.draw_paddle()
    ball.draw_ball()

    for block in blocks:
        block.draw_block()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()
    clock.tick()

    pygame.display.update()


run_game()
