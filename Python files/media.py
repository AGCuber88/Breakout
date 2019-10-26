from pygame import mixer
import pygame
pygame.display.init()

mixer.init()
mixer.music.load('ItsBoston - Arcade2.wav')
mixer.music.play(-1)


death_sound = mixer.Sound('bruh.wav')
paddle_bounce_sound = mixer.Sound('ball.wav')
block_bounce_sound = mixer.Sound('ball.wav')

#block_bounce_sound = mixer.Sound('Points.wav')
#paddle_bounce_sound = mixer.Sound('Bounce.wav')

