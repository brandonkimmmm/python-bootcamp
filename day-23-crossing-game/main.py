import time
from turtle import Screen, Turtle

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
print(player.shapesize())
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move, "Up")

screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
    if player.is_finished():
        scoreboard.increment_score()
        car_manager.increment_speed()
        player.reset()
    car_manager.generate_car()
    car_manager.move_cars()

scoreboard.game_over()

screen.exitonclick()
