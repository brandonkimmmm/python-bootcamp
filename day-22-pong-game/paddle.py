from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 260:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
