import turtle
from random import randint
 
 
number_of_turtle = 10
steps_of_the_time_number = 200
 
 
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtle)]     
 

for u in pool:
    u.penup()
    u.speed(50)
    u.goto(randint(-75, 75), randint(-75, 75))
    u.turtlesize(0.5)
    u.right(randint(0, 360))
 
 
for i in range(steps_of_the_time_number):
    for g in range(len(pool)):
        angle1 = pool[g].heading()  
        x1, y1 = pool[g].pos()      
        for h in range(len(pool)):  
            if g != h:
                x2, y2 = pool[h].pos()
                angle2 = pool[h].heading()
                x = abs(x1-x2)     
                y = abs(y1-y2)     
                if x < 8 and y < 8:     
                    pool[h].right(randint(1,180))   
                    pool[g].right(randint(1,180))
                    pool[h].forward(7)           
                    pool[g].forward(7) 
        if x1 < -80 or x1 > 80:          
            pool[g].seth(180 - angle1)
        elif y1 < -80 or y1 > 80:        
            pool[g].seth(-angle1)
        pool[g].forward(3)     
