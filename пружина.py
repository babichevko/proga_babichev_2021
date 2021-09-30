import turtle as t
t.shape('turtle')
t.speed(10)
import math
a=2
def d(r):
    b=math.pi*r/90
    for i in range(90):
        t.forward(b)
        t.right(a)
for i in range(4):
    d(50)
    d(10)
    
