import turtle as t
t.shape('turtle')
t.speed(10)
import math
a=2
def c(r):
    b=math.pi*r/90
    for q in range(180):
            t.forward(b)
            t.right(a)
def d(r):
    b=math.pi*r/90
    for i in range(90):
        t.forward(b)
        t.right(a)
t.fillcolor('yellow')
t.begin_fill()
c(100)
t.end_fill()
t.penup()
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(180)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
c(15)
t.end_fill()
t.penup()
t.forward(80)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
c(15)
t.end_fill()
t.penup()
t.backward(40)
t.right(90)
t.forward(30)
t.pendown()
t.width(15)
t.forward(40)
t.penup()
t.forward(10)
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
t.pencolor('red')
d(50)
