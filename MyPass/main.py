#!/usr/bin/python3
from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# pyperclip appears to have an issue in Debain

# ---------------------------- CONSTANTS -----------------------------------------#
BORDER = 20
HEIGHT = 200
WIDTH = 200
LOGO = "logo.png"
BLACK = "#000000"

DATA = "data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------------ #


def savepass():
    user_pass = pass_input.get()
    user_site = url_input.get()
    user_email = email_input.get()
    user_data = f"{user_site} | {user_email} | {user_pass}\n"

    if len(user_pass) == 0 or len(user_site) == 0:
        messagebox.showinfo(
            title="oopps", message=f"Please do not leave any empty fields.")
    else:
        is_ok = messagebox.askokcancel(
            title=user_site, message=f"Entered website details:\n\nEmail: {user_email} \nPassword: {user_pass}\n\nIs this OK to save? ")

        if is_ok:

            with open(DATA, 'a') as data:
                data.write(user_data)

            pass_input.delete(0, END)
            url_input.delete(0, END)


# ---------------------------- UI SETUP ----------------------------------------- #
# UI is a little off and could use some tweaking
window = Tk()
window.title("MyPass")
window.config(padx=BORDER, pady=BORDER)

lock_img = PhotoImage(file=LOGO)
canvas = Canvas(height=HEIGHT, width=WIDTH, highlightthickness=1)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

url = Label(fg=BLACK, text="Website: ")
url.grid(column=0, row=1)
url_input = Entry(width=38)
url_input.grid(column=1, row=1, columnspan=2)
url_input.focus()

email = Label(fg=BLACK, text="Email/Username: ")
email.grid(column=0, row=2)
email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "email@gmail.com")

pass_word = Label(fg=BLACK, text="Password: ")
pass_word.grid(column=0, row=3)
pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)
gen_pass = Button(text="Generate Password ", width=10, command=passgen)
gen_pass.grid(column=2, row=3)

pass_add = Button(text="Add", width=36, command=savepass)
pass_add.grid(column=1, row=4, columnspan=3)


window.mainloop()
