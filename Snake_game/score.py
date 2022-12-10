#!/usr/bin/python3

from turtle import Turtle
HEIGHT = 800
WIDTH = 1200
OFFSET = .35
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.goto(0, (HEIGHT*OFFSET)+75)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}           High Score: {self.high_score}", align=ALIGN,
                   font=FONT)

    def add_score(self):
        self.score += 1
        self.score_update()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", align=ALIGN, font=FONT)

    def score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
