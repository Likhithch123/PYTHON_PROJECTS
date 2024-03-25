from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        self.score=1
        self.create_scoreboard()
    
    def create_scoreboard(self):
        self.turtle=Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-250,250)
        self.turtle.write(f"Level: {self.score}",align="center",font=("Times New Roman",20,"normal"))
    
    def update_score(self):
        self.turtle.clear()
        self.score+=1
        self.turtle.write(f"Level: {self.score}",align="center",font=("Times New Roman",20,"normal"))
    
    def display_game_over(self):
        self.turtle.goto(0,0)
        self.turtle.write("GAME OVER",align="center",font=("Times New Roman",30,"normal"))
