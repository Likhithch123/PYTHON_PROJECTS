from turtle import Turtle
from random import randint,choice
TURTLE_COLORS = ["yellow", "gold", "orange","red", "maroon","violet","magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=5
class Car:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance=randint(1,7)
        if rand_chance==1:
            new_car=Turtle("square")
            new_car.color(choice(TURTLE_COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            rand_y=randint(-250,250)
            new_car.goto(300,rand_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increment_speed(self):
        self.car_speed+=MOVE_INCREMENT