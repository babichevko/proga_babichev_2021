<<<<<<< HEAD
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
chislo_ochkov = 0

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    parametry_kruga=[x, y, r]

def proverka_najatia(coordinaty_najatiya, parametry_kruga):

    for a,b in coordinaty_najatiya:
        cvadrat_rasstoiania=(x-a)**2 + (y-b)**2
    if cvadrat_rasstoiania>radius**2:
        print('мимо!')
    else:
        chislo_ochkov+=1



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    najal=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            if event.button == 1:
                najal=True
                new_ball()
                click(new_ball)

                proverka_najatia(parametry_kruga, event.pos)
                pygame.display.update()
                screen.fill(BLACK)
        if najal=False:
            new_ball()


print('ваши очки - ', chislo_ochkov)
pygame.quit()
=======

>>>>>>> origin/main
