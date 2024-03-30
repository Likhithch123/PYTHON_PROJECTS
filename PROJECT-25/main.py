import turtle
import pandas
from turtle import Screen
screen = Screen()
screen.title("India states game")
screen.addshape("image.gif")
turtle.shape("image.gif")
data = pandas.read_csv("india_states_csv.csv")
with open("high_score.txt") as file:
    high_score = file.read()
states_list = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{high_score} states correct",
                                    prompt="What's another state's name?").title()
    if answer_state in states_list:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_x = data[data.state == answer_state]["x"]
        new_y = data[data.state == answer_state]["y"]
        new_turtle.goto(int(new_x), int(new_y))
        new_turtle.write(f"{answer_state}", align="center", font=("Times New Roman", 10, "normal"))
        if int(high_score) < len(guessed_states):
            with open("high_score.txt", "w") as file:
                file.write(f"{len(guessed_states)}")
    else:
        break
screen.exitonclick()
