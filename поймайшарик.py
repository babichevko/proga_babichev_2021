import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
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
v=[]

for i in range(randint(6, 12)):
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    balls.append([color, x, y, r])
for i in range(len(balls)):
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    v.append([vx, vy])

def new_ball(color, x, y, r):
    circle(screen, color, (x, y), r)

def proverka_najatia(coordinaty_najatiya, coordinata_kruga_x, coordinata_kruga_y, radius_kruga):
    global najal
    najal = False
    coordinata_najatiya_x = coordinaty_najatiya[0]
    coordinata_najatiya_y = coordinaty_najatiya[1]

    #проверка попадания в шарик по теореме Пифагора
    cvadrat_rasstoiania = (coordinata_kruga_x - coordinata_najatiya_x) ** 2 + (coordinata_kruga_y - coordinata_najatiya_y) ** 2
    if cvadrat_rasstoiania < radius_kruga ** 2:
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
                for i in range(len(balls)):
                    proverka_najatia(event.pos, balls[i][1], balls[i][2], balls[i][3])
                    if najal == True:
                        x = randint(100, 700)
                        y = randint(100, 500)
                        r = randint(30, 50)
                        color = COLORS[randint(0, 5)]
                        balls[i] = [color, x, y, r]
                        vx = randint(-5, 5)
                        vy = randint(-5, 5)
                        v[i] = [vx, vy]
                        chislo_ochkov+=1
    for i in range(len(balls)):
            color, x, y, r = balls[i]
            new_ball(color, x, y, r)
    for i in range(len(balls)):
        balls[i][1] += v[i][0]
        balls[i][2] += v[i][1]

        if balls[i][1] - 2 * balls[i][3] < 0 or balls[i][1] + 2 * balls[i][3] > 1200:
            v[i][0] = -v[i][0]
        if balls[i][2] - 2 * balls[i][3] < 0 or balls[i][2] + 2 * balls[i][3] > 900:
            v[i][1] = -v[i][1]

    pygame.display.update()

    screen.fill(BLACK)

print('ваши очки:', chislo_ochkov)
pygame.quit()






