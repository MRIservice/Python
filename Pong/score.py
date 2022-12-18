#!/usr/bin/python3

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 350)
        self.write(f"{self.score_r}", True, align="center",
                   font=('Arial', 30, 'normal'))
        self.goto(-100, 350)
        self.write(f"{self.score_l}", True, align="center",
                   font=('Arial', 30, 'normal'))

    def left_score(self):
        self.score_l += 1
        self.update_score()

    def right_score(self):
        self.score_r += 1
        self.update_score()
