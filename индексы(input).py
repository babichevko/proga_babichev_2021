import turtle as t
t.speed=1
y=open(r'''C:\Users\konst\python\2l\input.txt''')
d0=[]
d4=[]
d1=[]
d7=[]
d2=[]
d3=[]
d5=[]
d6=[]
d8=[]
d9=[]
stroki=[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9]
for i in range(len(stroki)):
    stroki[i]=y.readline()
for i in range(len(stroki)):
    stroki[i]=stroki[i].split()
for i in range(len(stroki)):
    w=stroki[i]
    for a in range(len(w)):
        w[a]=int(w[a])
h=input('какой индекс напечатать?')
nn=h.split()
arr=[]
for i in nn:
    arr.append(int(i))   
t.penup()
t.backward(500)
t.pendown()
for i in arr:
    for z in range(len(stroki)):
        if i==z:
            nugnyekomandy=stroki[z]
            for p in range(len(nugnyekomandy)):
                if p % 2 == 0:
                    t.forward(nugnyekomandy[p])
                else:
                    t.right(nugnyekomandy[p])
            t.penup()
            t.forward(200)
            t.pendown()
