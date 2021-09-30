import turtle as t
import math
t.shape("turtle")
r=40
t.speed(5)
def u(n):
    global r
    w=180*(n-2)/n
    q=w/2
    a=180-w
    s=math.sin(math.pi/(n))
    b=2*r*s
    t.left(q)
    for i in range(n):
        t.forward(b)
        t.right(a)
    t.right(q)
    t.penup()
    t.backward(20)
    t.pendown()
    r+=20
for n in range(3,11,1):
    u(n)


    
        
    

    
