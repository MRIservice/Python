#!/usr/bin/python3

from turtle import Turtle

HEIGHT = 800
WIDTH = 1200
BUFFER = .4


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.x = 7
        self.y = 7
        self.penup()
        self.ball_speed = .04

    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= .9

    def bounce_y(self):
        self.y *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = .04
