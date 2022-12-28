#!/usr/bin/python3

from tkinter import *
import math

####################################################################
# note this program still has a bug as it does not stop after a reset
####################################################################


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1  # 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PIC = "tomato.png"
reps = 0
timer = None

HEIGHT = 600
WIDTH = 600

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)

    canvas.itemconfig(timer, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    # If the 8th rep BRAK
    if reps % 8 == 0:
        count_down(long_break)
        title.config(text="Long Break", fg=RED)

    # if 2nd 4th or 6th rep
    elif reps % 2 == 0:
        count_down(short_break)
        title.config(text="Break", fg=PINK)

    else:
        # If 1st, 3rd, 5th and 7th rep
        count_down(work)
        title.config(text="Work", fg=GREEN)
        timer.configuration(text="00:00", fill="white")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    minutes = math.floor(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")

    if count > 0:
        window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            marks += "✔"

        check_mark.config(text=marks)
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Study Application")
window.config(padx=50, pady=100, bg=YELLOW)
# window.minsize(WIDTH, HEIGHT)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title.grid(column=1, row=0)


canvas = Canvas(width=280, height=224, bg=YELLOW, highlightthicknes=0)
tomato = PhotoImage(file=PIC)
canvas.create_image(140, 112, image=tomato)
timer = canvas.create_text(143, 140, text="00:00", fill="white",
                           font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=2)

timer_start = Button(text="Start", command=start_timer)
timer_start.grid(column=0, row=4)

timer_reset = Button(text="Reset", command=reset)
timer_reset.grid(column=2, row=4)

check_mark = Label(fg=GREEN, font=(
    FONT_NAME, 30, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=5)


window.mainloop()
