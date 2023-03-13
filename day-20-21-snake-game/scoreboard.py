from os import path
from turtle import Turtle

FILE_PATH = f"{path.dirname(__file__)}/data.txt"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        if not path.isfile(FILE_PATH):
            file = open(FILE_PATH, mode="w")
            file.write("0")
            file.close()
        with open(FILE_PATH) as file:
            score = file.read()
            if score == "":
                score = "0"
            self.score = 0
            self.high_score = int(score)
            self.penup()
            self.color("white")
            self.hideturtle()
            self.goto(0, 270)
            self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
