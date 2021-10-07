import pygame
from pygame.draw import *

pygame.init()

sky_blue = (0, 255, 255)
grass_green = (0, 255, 0)
leaf_green = (0, 128, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
fruit_pink = (255, 170, 170)
pink = (229, 128, 255)
hair1 = (233, 175, 175)
hair2 = (233, 198, 175)
hair3 = (255, 238, 170)
hair4 = (229, 255, 128)
hair5 = (175, 233, 221)

FPS = 30
screen = pygame.display.set_mode((800, 1200))

#Здесь описаны все функции рисования

def sun(x_center, y_center, radius):
    circle(screen, yellow, (x_center, y_center), radius)
def grass(y, dlina, shirina):
    rect(screen, grass_green, (0, y, dlina, shirina))
def sky(dlina, shirina):
        rect(screen, sky_blue, (0, 0, dlina, shirina))


def tree(x, y, size_x, size_y):
    rect(screen, white, ((100 - 100) * size_x + x, (630 - 870) * size_y + y, 50 * size_x, 150 * size_y))

    ellipse(screen, leaf_green, ((20 - 100) * size_x + x, (510 - 870) * size_y + y, 225 * size_x, 175 * size_y))
    ellipse(screen, leaf_green, ((15 - 100) * size_x + x, (170 - 870) * size_y + y, 220 * size_x, 240 * size_y))
    ellipse(screen, grass_green, ((20 - 100) * size_x + x, (510 - 870) * size_y + y, 225 * size_x, 175 * size_y), 3)
    ellipse(screen, grass_green, ((15 - 100) * size_x + x, (170 - 870) * size_y + y, 220 * size_x, 240 * size_y), 3)
    ellipse(screen, leaf_green, ((-70 - 100) * size_x + x, (340 - 870) * size_y + y, 400 * size_x, 200 * size_y))
    ellipse(screen, grass_green, ((-70 - 100) * size_x + x, (340 - 870) * size_y + y, 400 * size_x, 200 * size_y), 3)

    ellipsy2 = [
        (fruit_pink, (10 - 100) * size_x + x, (440 - 870) * size_y + y, 30 * size_x, 30 * size_y),
        (fruit_pink, (170 - 100) * size_x + x, (240 - 870) * size_y + y, 30 * size_x, 30 * size_y),
        (fruit_pink, (275 - 100) * size_x + x, (455 - 870) * size_y + y, 30 * size_x, 30 * size_y),
        (fruit_pink, (210 - 100) * size_x + x, (640 - 870) * size_y + y, 30 * size_x, 30 * size_y)]

    for a, b, c, d, e, in ellipsy2:
        ellipse(screen, a, (b, c, d, e))

    ellipsy3 = [((10 - 100) * size_x + x, (440 - 870) * size_y + y, 30 * size_x, 30 * size_y), ((170 - 100) * size_x + x, (240 - 870) * size_y + y, 30 * size_x, 30 * size_y), ((275 - 100) * size_x + x, (455 - 870) * size_y + y, 30 * size_x, 30 * size_y), ((210 - 100) * size_x + x, (640 - 870) * size_y + y, 30 * size_x, 30 * size_y)]

    for b, c, d, e in ellipsy3:
        ellipse(screen, grass_green, (b, c, d, e), 3)

def pricheska_edinoroga(coord_x, coord_y, size):
    parametry_ellipsov=[(hair2, coord_x - 45 * size, coord_y + 12 * abs(size), 50 * abs(size), 30 * abs(size)), (hair1, coord_x - 65 * size, coord_y, 65 * abs(size), 20 * abs(size)), (hair1, coord_x - 95 * size, coord_y + 12 * abs(size), 65 * abs(size), 40 * abs(size)), (hair2, coord_x - 75 * size, coord_y + 60 * abs(size), 65 * abs(size), 30 * abs(size)), (hair3, coord_x - 110 * size, coord_y + 40 * abs(size), 90 * abs(size), 30 * abs(size)), (hair4, coord_x - 125 * size, coord_y + 60 * abs(size), 65 * abs(size), 25 * abs(size)), (hair4, coord_x - 72 * size, coord_y + 82 * abs(size), 85 * abs(size), 28 * abs(size)),  (hair3, coord_x - 115 * size, coord_y + 80 * abs(size), 60 * abs(size), 23 * abs(size)), (hair3, coord_x - 100 * size, coord_y + 95 * abs(size), 75 * abs(size), 20 * abs(size)), (hair5, coord_x - 133 * size, coord_y + 90 * abs(size), 45 * abs(size), 15 * abs(size)), (hair5, coord_x - 133 * size, coord_y + 100 * abs(size), 70 * abs(size), 18 * abs(size)), (hair3, coord_x - 95 * size, coord_y + 105 * abs(size), 70 * abs(size), 20 * abs(size)), (hair5, coord_x - 65 * size, coord_y + 105 * abs(size), 62 * abs(size), 23 * abs(size)), (pink, coord_x - 160 * size, coord_y + 113 * abs(size), 90 * abs(size), 22 * abs(size))]
    for a,b,c,d,e in parametry_ellipsov:
        ellipse(screen, a, (b, c, d, e))
def nogi_edinoroga(x, y, size):
    parametry_nog=[((565 - 645) * size + x, (670 - 655) * size + y, 90 * size, 130 * size), ((395 - 645) * size + x, (845 - 655) * size + y, 20 * size, 155 * size), ((465 - 645) * size + x, (860 - 655) * size + y, 25 * size, 130 * size), ((565 - 645) * size + x, (870 - 655) * size + y, 22 * size, 150 * size), ((625 - 645) * size + x, (850 - 655) * size + y, 18 * size, 140 * size)]
    for a,b,c,d in parametry_nog:
        rect(screen, white, (a, b, c, d))
def glaz_edinoroga(x, y, size):
    circle(screen, pink, ((640 - 645) * size + x, (655 - 655) * size + y), 13 * size)
    circle(screen, black, ((645 - 645) * size + x, (655 - 655) * size + y), 5 * size)
def rog_edinoroga(x,y,size):
    polygon(screen, pink,
            [((606 - 645) * size + x, (621 - 655) * size + y), ((633 - 645) * size + x, (500 - 655) * size + y),
             ((635 - 645) * size + x, (625 - 655) * size + y)])

def telo_edinoroga(x, y, size):
    parametry_ellipsov=[(white, (375 - 645) * size + x, (750 - 655) * size + y, 310 * size, 130 * size), (white, (565 - 645) * size + x, (620 - 655) * size + y, 110 * size, 75 * size), (white, (620 - 645) * size + x, (645 - 655) * size + y, 100 * size, 50 * size), (hair1, (575 - 645) * size + x, (610 - 655) * size + y, 50 * size, 30 * size), (white, (633 - 645) * size + x, (650 - 655) * size + y, 10 * size, 3 * size)]
    for a,b,c,d,e in parametry_ellipsov:
        ellipse(screen, a, (b,c,d,e))
    nogi_edinoroga(x, y, size)
    glaz_edinoroga(x, y, size)
    rog_edinoroga(x, y, size)

def edinorog(x, y, size):
    telo_edinoroga(x,y,size)
    volosy = [((190 - 645) * size + x, (860 - 655) * size + y, - size),
              ((390 - 645) * size + x, (810 - 655) * size + y, size),
              ((604 - 645) * size + x, (630 - 655) * size + y, size)]
    for A, B, C in volosy:
        pricheska_edinoroga(A, B, C)






#Здесь рисуем всё что нужно

sky(800, 520)
grass (520, 800, 1200)
sun (770, 120, 150)

for i in range(150):
    circle(screen, (255, 255, 155 - i), (770, 120), 150 - i)


trees = [(220, 600, 1, 1), (350, 640, 0.7, 0.3), (165, 870, 1, 0.7), (40, 750, 0.7, 0.7), (70, 1100, 0.7, 0.7)]
edinorogi = [(400, 800, 0.9), (675, 655, 0.5), (550, 450, 0.6), (750, 480, 0.3), (710, 900, 0.6)]

for a,b,c,d in trees:
    tree(a, b, c, d)
for a, b, c in edinorogi:
    edinorog(a, b, c)



pygame.display.update()
clock = pygame.time.Clock()
finished = False



while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
