#!/usr/bin/python3
from turtle import Turtle
import random

HEIGHT = 800
WIDTH = 1200
OFFSET = .48


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5)
        self.color("red")
        self.speed("fastest")
        self.fresh_food()

    def fresh_food(self):
        rand_y = random.randint(-HEIGHT*OFFSET, HEIGHT*OFFSET)
        rand_x = random.randint(-WIDTH*OFFSET, WIDTH*OFFSET)
        self.goto(rand_x, rand_y)
