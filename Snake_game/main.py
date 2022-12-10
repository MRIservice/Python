#!/usr/bin/python3

from turtle import Screen
from food import Food
from snake import Snake
from score import Score
import time

HEIGHT = 800
WIDTH = 1200
OFFSET = .49

START = [(0, 0), (-20, 0), (-40, 0)]

full_snake = []

game_on = True

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("SNAKE!!!")
screen.tracer(0)


food = Food()
score = Score()

snake = Snake()
snake.make_snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:

    screen.update()
    time.sleep(.1)
    snake.move_snake()

# Detect colision with food
    if snake.head.distance(food) < 15:
        food.fresh_food()
        score.add_score()
        snake.grow_snake()
        

# Detect wall crash
    if snake.head.ycor() > HEIGHT * OFFSET or snake.head.ycor() < -HEIGHT * OFFSET or snake.head.xcor() > WIDTH * OFFSET or snake.head.xcor() < -WIDTH * OFFSET:
        game_on = False
        score.game_over()

# Detect tail colision
    for seg in full_snake[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
