#!/usr/bin/python3

# Flash card APP

from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"

BACK_IMG = "./images/card_back.png"
FRONT_IMG = "./images/card_front.png"
RIGHT_IMG = "./images/right.png"
WRONG_IMG = "./images/wrong.png"
CSV = "./data/french_words.csv"
CSV_TO_LEARN = "./data/words_to_learn.csv"

WIDTH = 800
HEIGHT = 536

FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")

# card = {} this current card does not appear to be needed


def next_card():
    global card, timer

    # Reset timer from flipping cards after new card selected
    window.after_cancel(timer)
    card = random.choice(words_to_learn)
    canvas.itemconfig(word, text=card[french], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(background, image=front_img)
    
    # change/flip card every time
    timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(word, text=card[english], fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(background, image=back_img)


def known_word():
    words_to_learn.remove(card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv(CSV_TO_LEARN, index=False)

    next_card()


# Set up Window
window = Tk()
window.title("Flash Card App")
# window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip)

# Images used
back_img = PhotoImage(file=BACK_IMG)
front_img = PhotoImage(file=FRONT_IMG)
right_img = PhotoImage(file=RIGHT_IMG)
wrong_img = PhotoImage(file=WRONG_IMG)

# Canvas setup
# Make the canvas the same size as the image used
canvas = Canvas(width=WIDTH, height=HEIGHT,
                bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(WIDTH/2, HEIGHT/2, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(
    400, 150, text="", fill="black", font=FONT1)
word = canvas.create_text(
    400, 263, text="", fill="black", font=FONT2)


# convert csv to dictionary
try:
    data = pandas.read_csv(CSV_TO_LEARN)                    # Does File Exist?

except FileNotFoundError:
    data = pandas.read_csv(CSV)   # File not found *****  use this file instead
    words_to_learn = data.to_dict(orient="records")     # Create Dictionary
    french = data.columns.values[0]                     # French
    english = data.columns.values[1]                    # English

else:
    words_to_learn = data.to_dict(orient="records")     # Create dictionary
    french = data.columns.values[0]                     # French
    english = data.columns.values[1]                    # English

# Buttons
known_button = Button(
    image=right_img, highlightthickness=0, command=known_word)
unknown_button = Button(
    image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button.grid(row=1, column=1)

next_card()


# print(words_to_learn)
# print(len(words_to_learn))
# print(card)


window.mainloop()
