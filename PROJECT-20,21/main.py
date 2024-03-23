from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
import snake
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game.")
my_screen.tracer(0)
snake_obj = snake.Snake()
food_obj = Food()
score_obj = Scoreboard()
my_screen.listen()
my_screen.onkey(snake_obj.up, "Up")
my_screen.onkey(snake_obj.down, "Down")
my_screen.onkey(snake_obj.left, "Left")
my_screen.onkey(snake_obj.right, "Right")
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake_obj.move()
    # Detect collision with food.
    if snake_obj.head.distance(food_obj) < 15:
        food_obj.refresh()
        snake_obj.extend()
        score_obj.increase_score()
    # Detect collision with wall.
    if (snake_obj.head.xcor() > 290 or snake_obj.head.xcor() < -290 or
            snake_obj.head.ycor() > 290 or snake_obj.head.ycor() < -290):
        game_is_on = False
        score_obj.game_over()
    # Detect collision with tail.
    # Snake hits its head segment with it's any other segment
    for turtle in snake_obj.all_turtles[1:]:
        if snake_obj.head.distance(turtle) < 10:
            game_is_on = False
            score_obj.game_over()
my_screen.exitonclick()
