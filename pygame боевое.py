import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1100))

p = [(0, 0, 200, 0, 100), (150, 100, 250, 100, 50), (250, 150, 250, 150, 100), (200, 50, 150, 250, 150),
     (250, 150, 0, 400, 100), (0, 100, 150, 500, 600)]
for q, b, c, d, e in p:
    rect(screen, (q, b, c), (0, d, 800, e))


def ptica(a, b):
    fot = [(a, b, 175, 75), (a + 150, b + 15, 75, 35), (a + 200, b, 50, 30), (a + 55, b + 50, 25, 75),
           (a + 75, b + 50, 25, 60), (a + 65, b + 115, 70, 17), (a + 85, b + 100, 70, 17)]
    dot = [(a + 125, b + 100, 30, 5), (a + 125, b + 104, 40, 5), (a + 125, b + 108, 30, 5), (a + 120, b + 115, 30, 5),
           (a + 120, b + 119, 40, 5), (a + 120, b + 123, 30, 5)]

    pygame.draw.polygon(screen, (250, 200, 100),
                        [(a + 245, b + 20), (a + 285, b + 28), (a + 295, b + 20), (a + 285, b + 12), (a + 235, b + 18),
                         (a + 235, b + 20)])

    pygame.draw.aaline(screen, (0, 0, 0), (a + 235, b + 19), (a + 295, b + 20), 1)

    pygame.draw.polygon(screen, (255, 255, 255),
                        [(a + 125, b + 20), (a - 55, b - 60), (a - 75, b + 10), (a + 25, b + 30), (a + 25, b + 20)])
    pygame.draw.polygon(screen, (255, 255, 255),
                        [(a + 125, b + 20), (a - 55, b - 60), (a - 75, b + 10), (a + 25, b + 30), (a + 25, b + 20)], 1)
    pygame.draw.ellipse(screen, (0, 0, 0), [a + 65, b + 115, 70, 17], 1)
    pygame.draw.ellipse(screen, (0, 0, 0), [a + 85, b + 100, 70, 17], 1)

    pygame.draw.polygon(screen, (255, 255, 255),
                        [(a + 125, b + 10), (a + 85, b - 80), (a - 85, b - 150), (a - 35, b - 70), (a + 105, b + 10),
                         (a + 125, b + 10)])
    pygame.draw.polygon(screen, (0, 0, 0),
                        [(a + 125, b + 10), (a + 85, b - 80), (a - 85, b - 150), (a - 35, b - 70), (a + 105, b + 10),
                         (a + 125, b + 10)], 1)
    pygame.draw.polygon(screen, (255, 255, 255),
                        [(a + 125, b + 10), (a + 85, b - 80), (a - 85, b - 150), (a - 35, b - 70), (a + 105, b + 10),
                         (a + 125, b + 10)])
    pygame.draw.polygon(screen, (0, 0, 0),
                        [(a + 125, b + 10), (a + 85, b - 80), (a - 85, b - 150), (a - 35, b - 70), (a + 105, b + 10),
                         (a + 125, b + 10)], 1)
    for s, q, c, d in fot:
        pygame.draw.ellipse(screen, (255, 255, 255), (s, q, c, d))
    pygame.draw.circle(screen, (0, 0, 0), (a + 225, b + 10), 5)

    for a, b, c, d, e, f in [
        ((a + 75, b + 10), (a + 25, b - 80), (a - 145, b - 150), (a - 95, b - 70), (a + 55, b + 10), (a + 75, b + 10))]:
        pygame.draw.polygon(screen, (255, 255, 255), [a, b, c, d, e, f])
        pygame.draw.polygon(screen, (0, 0, 0), [a, b, c, d, e, f], 1)

    for s, q, c, d in dot:
        pygame.draw.ellipse(screen, (250, 200, 50), (s, q, c, d))
        pygame.draw.ellipse(screen, (0, 0, 0), (s, q, c, d), 1)


def ryba(a, b):
    mass = [((a + 300, b + 127), (a + 285, b + 145), (a + 315, b + 150), (a + 310, b + 130), (a + 300, b + 127)),
            ((a + 345, b + 127), (a + 355, b + 145), (a + 370, b + 150), (a + 350, b + 130), (a + 345, b + 126)),
            ((a + 325, b + 100), (a + 350, b + 103), (a + 350, b + 90), (a + 305, b + 85), (a + 325, b + 100))]
    mass2 = [((a + 275, b + 113), (a + 245, b + 90), (a + 245, b + 140), (a + 275, b + 113)),
             ((a + 275, b + 113), (a + 245, b + 90), (a + 245, b + 140), (a + 275, b + 113))]

    pygame.draw.arc(screen, (100, 150, 0), (a + 275, b + 100, 100, 50), 0.4, 2.74, 40)
    pygame.draw.arc(screen, (100, 150, 0), (a + 275, b + 80, 100, 50), 3.44, 6, 40)
    pygame.draw.circle(screen, (0, 0, 0), (a + 350, b + 112), 5)
    pygame.draw.circle(screen, (255, 255, 255), (a + 350, b + 112), 2)

    for a, b, c, d in mass2:
        pygame.draw.polygon(screen, (0, 150, 50), [a, b, c, d])
        pygame.draw.polygon(screen, (0, 150, 50), [a, b, c, d], 1)
    for a, b, c, d, e in mass:
        pygame.draw.polygon(screen, (150, 100, 100), [a, b, c, d, e])
        pygame.draw.polygon(screen, (0, 0, 0), [a, b, c, d, e], 1)


def ptichka(a, b, c, d):
    pygame.draw.arc(screen, (255, 255, 255), (a, b, c, d), 0, 3.14, 5)
    pygame.draw.arc(screen, (255, 255, 255), (a + c, b, c, d), 0, 3.14, 5)


ptichki = [(500, 270, 50, 20), (200, 420, 70, 30), (100, 200, 50, 30)]

ptica(200, 700)
ryba(300, 700)
for a, b, u, d in ptichki:
    ptichka(a, b, u, d)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
