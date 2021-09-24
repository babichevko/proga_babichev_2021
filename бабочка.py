import turtle as t
t.speed(100)
import math
t.shape('turtle')
a=2
def c(r):
    global q
    b=2*math.pi*r/180
    for q in range(180):
            t.forward(b)
            t.left(a)
    for p in range(180):
            t.forward(b)
            t.right(a)
for r in range (20,50,3):
    c(r)
