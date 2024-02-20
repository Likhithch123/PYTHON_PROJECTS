import turtle
from turtle import Turtle, Screen
from random import randint
turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.hideturtle()
timmy.penup()
timmy.forward(300)
timmy.setheading(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

for i in range(10):
    for _ in range(10):
        timmy.dot(20, random_color())
        timmy.forward(50)
    if i%2==0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(50)
    else:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
        timmy.forward(50)
my_screen = Screen()
my_screen.exitonclick()
