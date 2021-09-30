import pygame 
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

rect(screen, (200, 50, 200), (50, 50, 500, 500))
circle(screen, (255, 255, 0), (300, 300), 200)
circle(screen, (255, 0, 0), (230, 250), 50)
circle(screen, (255, 0, 0), (370, 250), 40)
circle(screen, (0, 0, 0), (230, 250), 25)
circle(screen, (0, 0, 0), (370, 250), 15)
rect(screen, (0, 0, 0), (150, 375, 300, 40))
line(screen, (0,0,0), (120,120), (280, 215), 20)
line(screen, (0,0,0), (450,150), (300, 225), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
