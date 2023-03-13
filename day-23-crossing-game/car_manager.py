from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=320, y=y_pos)
        self.color(choice(COLORS))
        self.setheading(180)

    def move(self, speed):
        self.forward(speed)


class CarManager:
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        random_change = randint(1, 6)
        if random_change == 1:
            y_pos = randint(-250, 250)
            self.cars.append(Car(y_pos))

    def move_cars(self):
        for car in self.cars:
            car.move(self.move_speed)

    def increment_speed(self):
        self.move_speed += MOVE_INCREMENT
