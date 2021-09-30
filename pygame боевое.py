import pygame 
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1100))

a=[(0,0,200,0,100),(150,100,250,100,50),(250,150,250,150,100),(200,50,150,250,150),(250,150,0,400,100),(0,100,150,500,600)]
for q,b,c,d,e in a:
        rect(screen, (q, b, c), (0, d, 800, e))
b=[(225, 700, 175, 75), (375, 715, 75, 35), (425,700,50,30), (280,750,25,75),(300,750,25,60), (290,815,70,17),(310,800,70,17)]
for a,q,c,d in b:
        pygame.draw.ellipse(screen, (255,255,255), (a,q,c,d))
c=[(500, 270, 50, 20, 0,3),(550, 270, 50, 20, 0,3), (200, 420, 70, 30, 0,3),(270, 420, 70, 30, 0,3),(100, 200, 50, 30,  0,3),(150, 200, 50, 30, 0, 3.2)]
for z,x,c,v,s,d in c:
        pygame.draw.arc(screen, (255,255,255), (z,x,c,v),s,d,5)
pygame.draw.polygon(screen, (250,200,100), [(470,720), (510,728), (520, 720), (510,712), (460,718), (460,720)])
pygame.draw.aaline(screen, (0,0,0), (460,719), (520,720), 1)
pygame.draw.circle(screen, (0,0,0), (450, 710), 5)
pygame.draw.polygon(screen, (255,255,255), [(250,720), (170,640), (150, 710), (250,730), (250,720)])
pygame.draw.arc(screen, (50,200,50), ())


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
