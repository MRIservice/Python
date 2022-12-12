#!/usr/bin/python3

from turtle import Turtle

FONT = ("Courier", 24, "normal")

HEIGHT = 800
WIDTH = 1200
BUFFER = .45


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-WIDTH * BUFFER, HEIGHT * BUFFER)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.score}", align="left", font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!", align="center", font=FONT)
