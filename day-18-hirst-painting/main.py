from random import choice
from turtle import Screen, Turtle, colormode

color_list = [
    (188, 19, 46),
    (244, 233, 64),
    (252, 232, 237),
    (217, 239, 245),
    (195, 76, 34),
    (218, 66, 106),
    (13, 143, 89),
    (18, 125, 173),
    (196, 176, 17),
    (108, 182, 209),
    (12, 167, 214),
    (208, 154, 91),
    (238, 232, 3),
    (25, 40, 75),
    (36, 43, 111),
    (78, 175, 96),
    (181, 44, 65),
    (217, 67, 47),
    (217, 129, 153),
    (125, 185, 120),
    (238, 161, 180),
    (7, 61, 38),
    (147, 209, 220),
    (8, 91, 52),
    (5, 86, 109),
    (160, 30, 27),
    (237, 170, 163),
    (158, 211, 188),
]

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setpos(-300, -300)

for num in range(10):
    current_pos = tim.position()
    tim.setpos(-300, (current_pos[1] + 50))
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)

screen = Screen()
screen.exitonclick()
