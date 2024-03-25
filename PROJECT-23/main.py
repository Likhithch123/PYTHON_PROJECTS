from turtle import Screen
from player import Player
from carmanager import Car
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game.")
screen.tracer(0)
screen.listen()
player_obj=Player()
car_obj=Car()
score_obj=Scoreboard()
screen.onkey(player_obj.go_up,"Up")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_obj.create_car()
    car_obj.move_cars()

    # Detect when our turtle collides with the cars.
    for car in car_obj.all_cars:
        if player_obj.distance(car) < 20:
            game_is_on=False
            score_obj.display_game_over()

    # Detect when turtle reaches the other side.
    if player_obj.is_at_finish_line(): 
        player_obj.go_to_start()
        car_obj.increment_speed()
        score_obj.update_score()
    
screen.exitonclick()