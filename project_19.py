from turtle import Turtle, Screen
from random import randint
is_race_on = False
turtle_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
my_screen = Screen()
my_screen.setup(height=500, width=500)
user_guess = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_guess:
    is_race_on = True

all_turtles = []
y = -150
x = -230
for i in range(6):
    new_turtle = Turtle("turtle")
    color = turtle_colors[i]
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    all_turtles.append(new_turtle)
    y += 50

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if user_guess == turtle.pencolor():
                print("You won!")
            else:
                print("You lose.")
            print(f"{turtle.pencolor()} turtle won the race.")
            is_race_on = False
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
my_screen.exitonclick()
