#!/usr/bin/python3

import pandas
import turtle


#HEIGHT = 800
#WIDTH = 1200
BACKGROUND = "./blank_states_img.gif"
CSV_IN = "./50_states.csv"
CSV_OUT = "./states_missed.csv"

data = pandas.read_csv(CSV_IN)

screen = turtle.Screen()
screen.title("STATES GUESSING GAME")
# screen.bgpic(BACKGROUND)
screen.addshape(BACKGROUND)

turtle.shape(BACKGROUND)


# Print cordinates and keep program/loop running
# def mouse_cordinates(x, y):
#     print(x, y)

# turtle.onscreenclick(mouse_cordinates)

# screen.exitonclick()
# turtle.mainloop()

data = pandas.read_csv(CSV_IN)

state_list = data.state.to_list()
guessed = []
missed = []

while len(guessed) < 50:

    answer = screen.textinput(
        title=f"{len(guessed)} /50 correct answers",  prompt="Name another state").title()

    if answer == "Exit":
        missied = [state for state in state_list if state not in guessed]
        # for state in state_list:
        #     if state not in guessed:
        #         missed.append(state)
        new_data = pandas.DataFrame(missed)
        new_data.to_csv(CSV_OUT)
        break

    if answer in state_list:
        pod = turtle.Turtle()
        guessed.append(answer)
        pod.hideturtle()
        pod.penup()
        state_data = data[data.state == answer]
        pod.goto(int(state_data.x), int(state_data.y))
        pod.write(answer)


print(missed)
# screen.exitonclick()
