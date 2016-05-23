import turtle
t = turtle.Turtle()

length = int(input('Enter a size'))
degree = int(input('Enter a degree'))

screen = turtle._Screen
while True:
    t.forward(length)
    t.left(degree)