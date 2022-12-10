#!/usr/bin/python3

from turtle import Turtle, heading, setheading

HEIGHT = 800
WIDTH = 1200
OFFSET = .48

MOVE = 20
START = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.full_snake = []
        self.make_snake()
        self.head = self.full_snake[0]

    def make_snake(self):
        for location in START:
            self.create_segment(location)

    def create_segment(self, location):
        snake = Turtle('square')
        snake.color("aqua")
        snake.penup()
        snake.goto(location)
        self.full_snake.append(snake)

    def grow_snake(self):
        self.create_segment(self.full_snake[-1].position())

    def move_snake(self):
        for part in range(len(self.full_snake)-1, 0, -1):
            new_x = self.full_snake[part-1].xcor()
            new_y = self.full_snake[part-1].ycor()
            self.full_snake[part].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
