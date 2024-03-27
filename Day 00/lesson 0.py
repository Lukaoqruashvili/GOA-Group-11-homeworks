from turtle import *


# we want to paint a house

#step 1: draw a square
speed(50)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

# drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50, 110)
pendown()

color("brown")
width(3)
right(150)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)


penup()
goto(150, 110)
pendown()

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

penup()
goto(30, 150)
pendown()

forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

# windows done

exitonclick()