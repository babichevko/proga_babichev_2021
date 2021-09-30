import turtle as t
t.speed(50)
t.penup()
t.backward(500)
t.pendown()
q=100
a=90
d0=[(0,a),(2*q,a),(q,a),(2*q,a),(q,0)]
d1=[(0,3*a/2),(1.41*a,2*a),(1.41*a,3*a/2),(2*q,2*a),(2*q,a)]
d2=[(0,2*a),(q,2*a),(q,a),(q,a),(q,-a),(q,-a),(q,2*a),(q,a),(q,a),(q,-a),(q,a)]
d3=[(0,2*a),(q,2*a),(q,a),(q,a),(q,2*a),(q,a),(q,a),(q,2*a),(q,-a),(2*q,a)]
d4=[(0,a),(2*q,2*a),(q,-a),(q,a),(q,2*a),(q,-a),(q,-a),(q,a)]
d5=[(0,2*a),(q,-a),(q,-a),(q,a),(q,a),(q,2*a),(q,-a),(q,-a),(q,a),(q,a),(q,0)]
d6=[(0,2*a),(q,-a),(2*q,-a),(q,-a),(q,-a),(q,a),(q,a), (q,0)]
d7=[(0,2*a),(q,2*a),(q,3*a/2),(1.41*q,-a/2),(q,2*a),(q,a/2),(1.41*q,a/2)]
d8=[(0,a),(2*q,a),(q,a),(2*q,a),(q,a),(q,a),(q,a),(q,a),(q,0)]
d9=[(0,2*a),(q,-a),(q,-a),(q,a),(q,a),(q,2*a),(q,-a),(2*q,a)]
h=input('какой индекс напечатать?')
nn=h.split()
arr=[]
t.speed(5)
for i in nn:
    arr.append(float(i))
komandy=[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9]
for i in arr:
    for z in range(len(komandy)):
        if i==z:
            for p,q in komandy[z]:
                t.forward(p)
                t.right(q)
            t.penup()
            t.forward(200)
            t.pendown()
    
