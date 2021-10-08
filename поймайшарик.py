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
global chislo_ochkov
chislo_ochkov = 0

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def proverka_najatia(coordinaty_najatiya, c, d, e):
    global najal
    najal = False
    a=coordinaty_najatiya[0]
    b=coordinaty_najatiya[1]
    cvadrat_rasstoiania=(c-a)**2 + (d-b)**2
    if cvadrat_rasstoiania > e**2:
        print('мимо!')
    else:
        najal = True
        print('молодец!')


new_ball()
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            if event.button == 1:
                proverka_najatia(event.pos, x, y, r)
                screen.fill(BLACK)
                pygame.display.update()
                new_ball()
                pygame.display.update()
                if najal == True:
                    chislo_ochkov+=1
print(chislo_ochkov)
pygame.quit()






