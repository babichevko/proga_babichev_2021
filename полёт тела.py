import turtle as t
t.speed(5)
ay=0.5
uy=10
c=0.1
ux=4
x=0
y=0
for i in range(2000):
    x += float(ux*c)
    y += float(uy*c - ay*c**2/2)
    if y>0:
        t.goto(x,y)
        uy=uy - ay*c
    else:
        uy=-uy*0.7
        
    
