from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball_obj = Ball()

score_obj = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball_obj.move_speed)
    screen.update()
    ball_obj.move_ball()

    # Detect collision with wall.
    if ball_obj.ycor() > 280 or ball_obj.ycor() < -280:
        ball_obj.bounce_y()

    # Detect collision with paddle.
    if ((ball_obj.distance(r_paddle) < 60 and ball_obj.xcor() > 320)
            or (ball_obj.distance(l_paddle) < 60 and ball_obj.xcor() < -320)):
        ball_obj.bounce_x()

    # Detect when r_paddle misses.
    if ball_obj.xcor() >= 380:
        ball_obj.restart()
        score_obj.l_point()

    # Detect when l_paddle misses.
    if ball_obj.xcor() <= -380:
        ball_obj.restart()
        score_obj.r_point()

screen.exitonclick()
