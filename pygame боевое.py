import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1100))


a=[(0,0,200,0,100),(150,100,250,100,50),(250,150,250,150,100),(200,50,150,250,150),(250,150,0,400,100),(0,100,150,500,600)]
for q,b,c,d,e in a:
        rect(screen, (q, b, c), (0, d, 800, e))

pygame.draw.polygon(screen, (0,150,50), [(500,813), (470,790), (470, 840), (500,813)])
pygame.draw.polygon(screen, (0,0,0), [(500,813), (470,790), (470, 840), (500,813)],1)

pygame.draw.polygon(screen, (255,255,255), [(350,710), (310,620), (140, 550), (190,630), (330,710), (350,710)])
pygame.draw.polygon(screen, (0,0,0), [(350,710), (310,620), (140, 550), (190,630), (330,710), (350,710)],1)

pygame.draw.polygon(screen, (255,255,255), [(250,720), (170,640), (150, 710), (250,730), (250,720)])


pygame.draw.polygon(screen, (255,255,255), [(300,710), (250,620), (80, 550), (130,630), (280,710), (300,710)])
pygame.draw.polygon(screen, (0,0,0), [(300,710), (250,620), (80, 550), (130,630), (280,710), (300,710)],1)


b=[(225, 700, 175, 75), (375, 715, 75, 35), (425,700,50,30), (280,750,25,75),(300,750,25,60), (290,815,70,17), (310,800,70,17)]
for a,q,c,d in b:
        pygame.draw.ellipse(screen, (255,255,255), (a,q,c,d))

pygame.draw.ellipse(screen, (0,0,0), (290,815,70,17),1)
pygame.draw.ellipse(screen, (0,0,0), (310,800,70,17),1)

c=[(500, 270, 50, 20, 0,3),(550, 270, 50, 20, 0,3), (200, 420, 70, 30, 0,3),(270, 420, 70, 30, 0,3),(100, 200, 50, 30,  0,3),(150, 200, 50, 30, 0, 3.2)]
for z,x,c,v,s,d in c:
        pygame.draw.arc(screen, (255,255,255), (z,x,c,v),s,d,5)

pygame.draw.polygon(screen, (250,200,100), [(470,720), (510,728), (520, 720), (510,712), (460,718), (460,720)])
pygame.draw.aaline(screen, (0,0,0), (460,719), (520,720), 1)
pygame.draw.circle(screen, (0,0,0), (450, 710), 5)
pygame.draw.arc(screen, (100,150,0),(500,800,100,50), 0.4, 2.74,40)
pygame.draw.arc(screen, (100,150,0),(500,780,100,50), 3.44, 6,40)
pygame.draw.circle(screen, (0,0,0), (575, 812), 5)
pygame.draw.circle(screen, (255,255,255), (575, 812), 2)

for a,b,c,d,e in [((525,827), (510,845), (540, 850), (535,830), (525,827)),((570,827), (580,845), (595, 850), (575,830), (570,826)),((550,800), (575,803), (575, 790), (530,785), (550, 800))]:
        pygame.draw.polygon(screen, (150,100,100), [a, b, c, d, e])
for a,b,c,d,e in [((525,827), (510,845), (540, 850), (535,830), (525,827)),((570,827), (580,845), (595, 850), (575,830), (570,826)),((550,800), (575,803), (575, 790), (530,785), (550, 800))]:
	pygame.draw.polygon(screen, (0,0,0), [a, b, c, d, e], 1)
d=[(350,800,30,5),(350,804,40,5),(350,808,30,5),(345,815,30,5),(345,819,40,5),(345,823,30,5)]
for a,q,c,d in d:
	pygame.draw.ellipse(screen, (250,200,50), (a,q,c,d))
	pygame.draw.ellipse(screen, (0,0,0), (a,q,c,d),1)





pygame.display.update()
clock = pygame.time.Clock()
finished =False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
