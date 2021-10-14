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

"Массивы для параметров шаров и их скоростей"
balls = []
v=[]

"Функция создания параметров нового шара"
def new_ball():
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    balls.append([color, x, y, r])

"Функция отрисовки нового шара"
def draw_ball(color, x, y, r):
    circle(screen, color, (x, y), r)

"Функция присваивания скорости новому шару"
def ball_speed():
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    v.append([vx, vy])

"Функция проверки попадания игрока по шару"
def proverka_najatia(coordinaty_najatiya, coordinata_kruga_x, coordinata_kruga_y, radius_kruga):
    global najal
    najal = False
    coordinata_najatiya_x = coordinaty_najatiya[0]
    coordinata_najatiya_y = coordinaty_najatiya[1]

    # проверка попадания в шарик по теореме Пифагора
    cvadrat_rasstoiania = (coordinata_kruga_x - coordinata_najatiya_x) ** 2 + (
                coordinata_kruga_y - coordinata_najatiya_y) ** 2
    if cvadrat_rasstoiania < radius_kruga ** 2:
        najal = True
        print('молодец!')

"Создаём изначально несколько шаров"
for i in range(5, 10):
    new_ball()
for i in range(len(balls)):
    ball_speed()

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
                    "Если попали по шару - удаляем его, делаем новый, счёт увеличивается"
                    if najal == True:
                        new_ball()
                        #Заменяем старый шар на новый
                        balls[i] = balls[len(balls)-1]
                        balls.pop(len(balls)-1)
                        #Заменяем скорость старого шара на скорость нового
                        ball_speed()
                        v[i] = v[len(v) - 1]
                        v.pop(len(v) - 1)
                        chislo_ochkov+=1
    #Рисуем шары
    for i in range(len(balls)):
            color, x, y, r = balls[i]
            draw_ball(color, x, y, r)

    "Изменение положения шаров"
    for i in range(len(balls)):
        balls[i][1] += v[i][0]
        balls[i][2] += v[i][1]

        "Отражение шаров от стенок"
        if balls[i][1] - 2 * balls[i][3] < 0 or balls[i][1] + 2 * balls[i][3] > 1200:
            k = randint(5, 17)
            v[i][0] = -k * v[i][0] / 10
            "Ограничим скорость шариков"
            if v[i][0] < -30:
                v[i][0] = -5
            if v[i][0] > 30:
                v[i][0] = 5
        if balls[i][2] - 2 * balls[i][3] < 0 or balls[i][2] + 2 * balls[i][3] > 900:
            t = randint(5, 17)
            v[i][1] = -t * v[i][1] / 10
            "Ограничим скорость шариков"
            if v[i][1] < -30:
                v[i][1] = -5
            if v[i][1] > 30:
                v[i][1] = 5

    pygame.display.update()

    screen.fill(BLACK)

print('ваши очки:', chislo_ochkov)
pygame.quit()






