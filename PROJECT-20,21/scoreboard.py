from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score_file.txt", "r") as file:
            text = file.read()
        self.highest_score = int(text)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.write(f"Score: {self.score}    Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.highest_score < self.score:
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("high_score_file.txt", "w") as file:
            file.write(f"{self.highest_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
