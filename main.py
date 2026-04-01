from turtle import *
from math import *
from time import sleep

def raiz(x):
    return sqrt(x)

def f2(x):
    return 1/x

def f3(x):
    return x**2

def f4(x):
    return f3(x)-(5*x)+6

def f5(x):
    return x**3-x**2-x+1

t = Turtle()
t.speed(0)

# Plano cartesiano
def plano():
    t.color('black')
    t.pu()
    t.goto(-300,0)
    t.pd()
    t.goto(300,0)
    t.stamp()

    # Eixo dos y
    t.pu()
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.lt(90)
    t.stamp()

# Função raiz quadrada
plano()

t.color('red')
t.pu()
t.goto(0,raiz(0))
t.pd()
for x in range(1,301):
    t.goto(x,raiz(x*100))

sleep(2)
t.clear()

# Função 1/x
t.rt(90)
plano()

t.color('red')
t.pu()
t.goto(1,f2(0.001))
t.pd()
for x in range(2,300):
    t.goto(x,f2(x/1000))

t.pu()
t.goto(-300,f2(-1))
t.pd()
for x in range(-299,-2):
    t.goto(x,f2(x/1000))

sleep(2)
t.clear()

# Função x^2

t.rt(90)
plano()

t.color('red')
t.pu()
t.goto(-15*10,f3(-15))
t.pd()
for x in range(-14,16):
    t.goto(x*10,f3(x))

sleep(2)
t.clear()

# Função 5-x^2

t.rt(90)
plano()

t.color('red')
t.pu()
t.goto(-15*10,5-f3(-15))
t.pd()
for x in range(-14,16):
    t.goto(x*10,5-f3(x))

sleep(2)
t.clear()

# Função x^2-5x+6

t.rt(90)
plano()

t.color('red')
t.pu()
t.goto(-15*10,f4(-15))
t.pd()
for x in range(-14,16):
    t.goto(x*10,f4(x))

sleep(2)
t.clear()

# Função x^3 - x^2 - x + 1
t.rt(90)
plano()

t.color('red')
t.pu()
t.goto(-10*25,f5(-10))
t.pd()
for x in range(-9,11):
    t.goto(x*25,f5(x))

sleep(2)
t.clear()


mainloop()