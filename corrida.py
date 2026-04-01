from turtle import *
import random

# Corrida de Tartarugas
t1 = Turtle()
t1.shape("turtle")
t2 = Turtle()
t2.shape("turtle")

t1.speed(1)
t1.pu()
t1.color("red")
t1.goto(-200, 100)

t2.speed(1)
t2.pu()
t2.color("blue")
t2.goto(-200, 130)

for num in range(30):
    t1.fd(random.randint(5, 10))
    t2.fd(random.randint(5, 10))

colors = ['red','blue','green','black','orange']

def corrida(n):
    list=[]
    for i in range(1,n+1):
        t = Turtle()
        t.shape("turtle")
        t.speed(1)
        t.pu()
        t.color(random.choice(colors))
        t.goto(-200, 100+30*i)
        i=i+1
        list.append(t)
    for x in range(0,n+1):
        for num in range(30):
            list[x].fd(random.randint(5,10))
            x=x+1

#Incompleto ainda

            
corrida(3)



mainloop()