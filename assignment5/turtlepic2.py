import turtle as t
import random
t.width(1)
list=['blue','pink','gray','green','orange','yellow','red']
t.tracer(10)
t.bgcolor('black')
a=0
b=50
for i in range(150):
    a+=1/b
    t.pencolor(random.choice(list))
    t.circle(i,90)
    t.forward(i)
    t.right(270)
    t.circle(i,270)
    t.forward(i)
    t.right(180)
t.exitonclick()

