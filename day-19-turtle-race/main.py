from random import randint
from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=400, width=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []
winner = None

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230 and is_race_on:
            is_race_on = False
            winner = turtle.color()[0]
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost. The {winner} turtle is the winner!")

screen.exitonclick()
