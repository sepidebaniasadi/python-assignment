import turtle as t
x=int(input("How many sides do you want to have?"))
y=int(input("How long do you like the length of the sides?"))
color=input("enter color: ")
backg=input("enter color for bg: ")
t.bgcolor(backg)
t.speed(-1)
t.pencolor(color)
for i in range(x):
    t.forward(y)
    t.left(360/x)

t.exitonclick()