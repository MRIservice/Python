#!/usr/bin/python3

from turtle import Turtle


HEIGHT = 800
WIDTH = 1200
BUFFER = .47
FINISH = HEIGHT * BUFFER


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto_start()

    def move_frog(self):
        self.forward(20)

    def cross_line(self):
        if self.ycor() > FINISH:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(0, -HEIGHT*BUFFER)
        self.setheading(90)
