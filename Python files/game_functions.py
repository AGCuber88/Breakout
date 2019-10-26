import sys
from time import sleep

import pygame

import media
from block import Block


def get_number_blocks_x(settings, block_width):
    available_space_x = settings.screen_width
    number_blocks_x = int(available_space_x / (1.5 * block_width))
    return number_blocks_x


def get_number_rows(settings, paddle_height, block_height):
    available_space_y = (settings.screen_height - (2 * block_height) - paddle_height)
    number_rows = int(available_space_y / (3 * block_height))
    return number_rows


def create_block(settings, screen, block_number, row_number, blocks):
    block = Block(settings, screen)
    block_width = block.rect.width
    block.x = block_width + 1.1 * block_width * block_number
    block.rect.x = block.x
    block.rect.y = block.rect.height + 1.5 * block.rect.height * row_number
    blocks.add(block)


def create_section(settings, screen, paddle, blocks):
    block = Block(settings, screen)
    number_blocks_x = get_number_blocks_x(settings, block.rect.width)
    number_rows = get_number_rows(settings, paddle.rect.height, block.rect.height)

    for row_number in range(number_rows):
        for block_num in range(number_blocks_x):
            create_block(settings, screen, block_num, row_number, blocks)


def check_play_button(settings, screen, stats, play_button, ball, paddle, blocks, sb, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)

        stats.game_active = True
        stats.settings.block_points = 50
        stats.reset_stats()

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_balls()

        blocks.empty()
        create_section(settings, screen, paddle, blocks)

        ball.reset_ball()

        paddle.center_paddle()
        ball.moving_down = True


def check_keydown_events(event, paddle):
    if event.key == pygame.K_x or event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        paddle.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        paddle.moving_left = True


def check_keyup_events(event, paddle):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        paddle.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        paddle.moving_left = False


def check_events(paddle, settings, screen, stats, play_button, ball, blocks, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle)
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_p:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, ball, paddle, blocks, sb, mouse_x, mouse_y)


def change_ball_direction_paddle(paddle, ball, settings):
    collisions = check_ball_paddle_collisions(paddle, ball, settings)

    if collisions:
        media.paddle_bounce_sound.play()
        if ball.moving_left == True:
            ball.moving_left = True
        elif ball.moving_right == True:
            ball.moving_right = True
        else:
            if ball.rect.centerx < paddle.rect.centerx:
                ball.moving_left = True
            elif ball.rect.centerx > paddle.rect.centerx:
                ball.moving_right = True

        ball.moving_down = False
        ball.moving_up = True


def change_ball_direction_block(settings, screen, paddle, ball, blocks, stats, sb):
    collisions = check_ball_block_collisions(ball, blocks)

    if len(blocks) <= 0:
        sleep(0.5)

        stats.level += 1
        sb.prep_level()

        if stats.level == 2:
            settings.ball_speed_factor_x += 6
            settings.ball_speed_factor_y += 2
            settings.paddle_speed_factor = 7

        if stats.level == 3:
            settings.ball_speed_factor_x += 2
            settings.ball_speed_factor_y += 2
            settings.paddle_speed_factor += 2

        if stats.level == 3:
            settings.ball_speed_factor_x += 2
            settings.ball_speed_factor_y += 2
            settings.paddle_speed_factor += 2

        if stats.level >= 4:
            settings.ball_speed_factor_x += 2
            settings.ball_speed_factor_y += 2
            settings.paddle_speed_factor += 2

        stats.settings.block_points = (stats.level * 2) * 50

        blocks.empty()
        create_section(settings, screen, paddle, blocks)

        paddle.center_paddle()
        ball.reset_ball()

    if collisions:
        media.block_bounce_sound.play()
        for block in collisions:
            blocks.remove(block)

            if ball.moving_down:
                ball.moving_down = False
                ball.moving_up = True
            else:
                ball.moving_up = False
                ball.moving_down = True

        for blocks in collisions:
            stats.score += settings.block_points
            sb.prep_score()
        check_high_score(stats, sb)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_ball_paddle_collisions(paddle, ball, settings):
    collisions = pygame.sprite.collide_rect(paddle, ball)

    return collisions


def check_ball_block_collisions(ball, blocks):
    collisions = pygame.sprite.spritecollide(ball, blocks, True)

    return collisions


def ball_update(screen, paddle, ball, settings, blocks, stats, sb):
    change_ball_direction_paddle(paddle, ball, settings)
    change_ball_direction_block(settings, screen, paddle, ball, blocks, stats, sb)
    ball.update_ball()


def check_game_loss(ball, screen, stats, settings, paddle, blocks, sb):
    screen_rect = screen.get_rect()

    if ball.rect.bottom >= screen_rect.bottom:
        media.death_sound.play()
        if stats.lives_left > 0:
            stats.lives_left -= 1

            sb.prep_balls()

            sleep(0.5)

            paddle.center_paddle()
            ball.reset_ball()
        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)

            with open("Highscore.txt", "w") as file:
                file.write(str(stats.high_score))
