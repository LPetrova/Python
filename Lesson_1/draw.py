import turtle
t = turtle.Turtle()

i = 10

while True:
    turtle.color('red')
    if i % 10 == 0:
        turtle.forward(40)

        turtle.backward(40)
        turtle.color('green')
        turtle.left(i % 82)
        turtle.forward(10)
        turtle.right(i % 23)

    i+=2