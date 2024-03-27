from turtle import *

speed(50)

def square():
    for i in range(4):
        forward(200)
        left(90)

def movecursor(x,y):
    penup()
    goto(x, y)
    pendown()

square()

movecursor(0, 300)

square()

movecursor(-300, 0)

square()

movecursor(-300, 300)

square()

movecursor(0, -300)

square()

movecursor(-300, -300)

square()

exitonclick()