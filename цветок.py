import turtle as t
t.speed(100)
t.shape('turtle')
def c(n):
    b=n/100
    a=360/n
    for q in range(n):
            t.forward(b)
            t.left(a)
    for p in range(n):
            t.forward(b)
            t.right(a)
n=200
for i in range(3):
    c(n)
    t.right(60)

