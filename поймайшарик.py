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
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Ваши очки:', False, (0, 0, 0))


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

#Функция вывода счёта
def schet():
    schetchik = pygame.font.Font(None, 100)
    textsurface = schetchik.render(str(chislo_ochkov), False, RED)
    screen.blit(textsurface,(100, 100))

def zavershenie_igry():
    clock.tick(FPS)
    cenok = pygame.font.Font(None, 200)
    textsurface = cenok.render('Game Over', False, RED)
    screen.blit(textsurface, (200, 300))
    cenok2 = pygame.font.Font(None, 200)
    textsurface2 = cenok2.render('Ваши очки:', False, GREEN)
    screen.blit(textsurface2, (200, 450))
    cenok3= pygame.font.Font(None, 200)
    textsurface3 = cenok3.render(str(chislo_ochkov), False, BLUE)
    screen.blit(textsurface3, (500, 600))
    pygame.display.update()

"Создаём изначально несколько шаров"
for i in range(5, 10):
    new_ball()
for i in range(len(balls)):
    ball_speed()

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    g = 0
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
                        chislo_ochkov += 1
                        g = 1
            #Если не попали - число шаров увеличивается
            if g != 1:
                new_ball()
                ball_speed()
                g=0

    #И когда шаров слишком много - игра заканчивается
    if len(balls) > 20:
        finished = True

    schet()

    #Рисуем шары
    for i in range(len(balls)):
            color, x, y, r = balls[i]
            draw_ball(color, x, y, r)

    "Изменение положения шаров"
    for i in range(len(balls)):
        balls[i][1] += v[i][0]
        balls[i][2] += v[i][1]

        "Отражение шаров от стенок"
        if balls[i][1] - 2 * balls[i][3] < 0 and v[i][0] < 0 or balls[i][1] + 2 * balls[i][3] > 1200 and v[i][0] > 0:
            k = randint(5, 18)
            v[i][0] = -k * v[i][0] / 10
            "Ограничим скорость шариков"
            if v[i][0] < -30:
                v[i][0] = -5
            if v[i][0] > 30:
                v[i][0] = 5
        if balls[i][2] - 2 * balls[i][3] < 0 and v[i][1] < 0 or balls[i][2] + 2 * balls[i][3] > 1200 and v[i][1] > 0:
            t = randint(5, 18)
            v[i][1] = -t * v[i][1] / 10

            "Ограничим скорость шариков"
            if v[i][1] < -30:
                v[i][1] = 5
            if v[i][1] > 30:
                v[i][1] = -5



    pygame.display.update()

    screen.fill(BLACK)

for i in range(150):
    zavershenie_igry()

print('ваши очки:', chislo_ochkov)
pygame.quit()






