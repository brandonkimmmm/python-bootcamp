from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def increment_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        self.score = 1
        self.display_score()

    def game_over(self):
        self.goto((0, 0))
        self.write(arg="GAME OVER", align="center", font=FONT)
