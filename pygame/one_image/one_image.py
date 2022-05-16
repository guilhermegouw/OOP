import pygame
from pygame.locals import *
import sys


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball_image = pygame.image.load('images/ball.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill(BLACK)
    window.blit(ball_image, (100, 200))

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)