import pygame
from pygame.locals import *
import sys
import random


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball_image = pygame.image.load('images/ball.png') 

ballx = random.randrange(MAX_WIDTH)
bally = random.randrange(MAX_HEIGHT)
ball_rect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if ball_rect.collidepoint(event.pos):
                ballx = random.randrange(MAX_WIDTH)
                bally = random.randrange(MAX_HEIGHT)
                ball_rect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    
    window.fill(BLACK)
    window.blit(ball_image, (ballx, bally))

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)