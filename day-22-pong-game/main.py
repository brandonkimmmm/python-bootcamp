from time import sleep
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


screen.listen()


while game_is_on:
    sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -330
    ):
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()


screen.exitonclick()
