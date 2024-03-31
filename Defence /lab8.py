import pygame
import sys
from pygame.locals import *
import random
pygame.init()

W, H = 600, 400
FPS = 60
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = (188, 227, 82)
screen.fill(bg)
pygame.display.set_caption("Race")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False 
            pygame.quit()
            sys.exit()
    pygame.display.update()

#enemy




#car



#Game over
font = pygame.font.SysFont('comicsansms', 40)
text = font.render('Game Over', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)