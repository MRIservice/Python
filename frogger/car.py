#!/usr/bin/python3

import random
from turtle import Turtle, xcor

HEIGHT = 800
WIDTH = 1200
BUFFER = .40

COLORS = ["red", "blue", "green", "yellow", "orange", "aqua", "black"]

MOVE = random.randint(0, 10)

y_pos = random.randint(-HEIGHT*BUFFER, HEIGHT*BUFFER)
x_pos = WIDTH*.5


class Car():
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE

    def make_car(self):
        rand_num = random.randint(1, 9)  # Delay Loop START
        if rand_num == 5:                  # Delay Loop
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=4, outline=None)
            car.setheading(180)
            car.penup()
            car.goto(x_pos, random.randint(-HEIGHT*BUFFER, HEIGHT*BUFFER))
            self.cars.append(car)

    def car_move(self):
        for auto in self.cars:
            auto.forward(self.car_speed)       # forward/backward

    def speed_up(self):
        self.car_speed += MOVE
