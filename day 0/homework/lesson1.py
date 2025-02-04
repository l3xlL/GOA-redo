from turtle import *

# print("hello world")

speed(30)
width(5)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)

left(90)



forward(70)
color("yellow")
begin_fill()
left(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

# door

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


#windows

penup()
goto(130, 150)
color("pink")
pendown()

right(240)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)


#window1

penup()
goto(70, 150)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)






exitonclick()