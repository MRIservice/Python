#!/usr/bin/python3

from http.client import CannotSendRequest
from logging.config import listen
from turtle import Turtle, Screen, update
from frog import Frog
from car import Car
from score import Score
import time

HEIGHT = 800
WIDTH = 1200
BUFFER = .47

game_on = True

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Frogger")
screen.tracer(0)

car = Car()
frog = Frog()
score = Score()

screen.listen()
screen.onkey(frog.move_frog, "Up")

while game_on:
    update()
    time.sleep(.1)

    car.make_car()
    car.car_move()


# Detect colision with car
    for auto in car.cars:
        if auto.distance(frog) < 20:
            game_on = False
            score.game_over()

# Detect Sucessful crossing
    if frog.cross_line():
        frog.goto_start()
        car.speed_up()
        score.add_score()

screen.exitonclick()
