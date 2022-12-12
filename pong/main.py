#!/usr/bin/python3

from turtle import Turtle, Screen, distance
from paddle import Paddle
from ball import Ball
from score import Score
import time


HEIGHT = 800
WIDTH = 1200
BUFFER = .48

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-.45*WIDTH, 0))
r_paddle = Paddle((.45*WIDTH, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.ball_speed)

    # detect collision with wall
    if ball.ycor() > BUFFER * HEIGHT or ball.ycor() < -BUFFER * HEIGHT:
        ball.bounce_y()

    # detect contact between ball and paddle
    if ball.xcor() > .45*WIDTH and ball.distance(r_paddle) < 40 or ball.xcor() < -.45*WIDTH and ball.distance(l_paddle) < 40:
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > WIDTH * BUFFER:
        score.left_score()
        score.update_score()
        ball.reset()

    # detect left paddle miss
    if ball.xcor() < -WIDTH*BUFFER:
        score.right_score()
        score.update_score()
        ball.reset()

screen.exitonclick()
