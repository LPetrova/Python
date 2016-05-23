import turtle

side = 40
x = 1
y = 1
turtle.goto(x, y)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            turtle.begin_fill()

        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)


    turtle.penup()
    y = y + 40
    turtle.goto(x, y)
    turtle.pendown()

turtle.exitonclick()
