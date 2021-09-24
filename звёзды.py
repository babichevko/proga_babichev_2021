import turtle as t
t.speed(5)
def z(n):
    b=(n-2)*180/n
    a=180-b/3
    for i in range(n):
        t.forward(100)
        t.left(a)
z(5)
t.penup()
t.backward(150)
t.pendown()
z(11)
        
    
    
