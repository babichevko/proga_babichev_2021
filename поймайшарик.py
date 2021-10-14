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
balls = []

def new_ball():
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    dx = randint(5, 20)
    dy = randint(5, 20)
    balls.append([color, x, y, r, dx, dy])
    circle(screen, color, (x, y), r)

for i in range(randint(3, 10)):
    new_ball()

def proverka_najatia(coordinaty_najatiya, coordinata_kruga_x, coordinata_kruga_y, radius_kruga):
    global najal
    najal = False
    coordinata_najatiya_x = coordinaty_najatiya[0]
    coordinata_najatiya_y = coordinaty_najatiya[1]

#проверка попадания в шарик по теореме Пифагора
    cvadrat_rasstoiania = (coordinata_kruga_x - coordinata_najatiya_x) ** 2 + (coordinata_kruga_y - coordinata_najatiya_y) ** 2
    if cvadrat_rasstoiania > radius_kruga ** 2:
        print('мимо!')
    else:
        najal = True
        print('молодец!')

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('лови подлеца!')
            if event.button == 1:
                for i in balls:
                    proverka_najatia(event.pos, i[2], i[3], i[4])
                    if najal == True:
                        balls.pop(i)
                        x = randint(100, 700)
                        y = randint(100, 500)
                        r = randint(30, 50)
                        color = COLORS[randint(0, 5)]
                        balls.append([color, x, y, r])
                        pygame.display.update()
                        new_ball()
                        pygame.display.update()
                        chislo_ochkov+=1
                else:

                    pygame.display.update()

print('ваши очки:', chislo_ochkov)
pygame.quit()






