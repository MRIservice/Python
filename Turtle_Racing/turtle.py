#!/usr/bin/python3
import random
from turtle import Turtle, Screen

# Variables
WIDTH = 1200
HEIGHT = 800
WIDTH_EDGE = (WIDTH * .9) / 2
HEIGHT_EDGE = (HEIGHT * .8) / 2
race_on = False

COLORS = ["red", "blue", "green", "aqua", "yellow", "orange", "purple", "black"]
num_turtles = len(COLORS)
spacing = HEIGHT * .9 / num_turtles
all_turtles = []

# Set-up Screen
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Racing")
bet = screen.textinput("Place bets", "Which turtle will win? Enter Color ")

# Turtle


for color in COLORS:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-WIDTH_EDGE, HEIGHT_EDGE)
    HEIGHT_EDGE -= int(spacing)
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > WIDTH_EDGE:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == bet.lower():
                print(f"You won the winning color is {winning_color}")
            else:
                print(f"Sorry, you lost the winning color is {winning_color}")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

# Keep screen open
screen.exitonclick()
