FONT = ("Courier", 24, "normal")
from turtle import Screen, Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-270,270)
        self.hideturtle()
        self.color("black")
        self.update_score()
    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_score()
    def update_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)


