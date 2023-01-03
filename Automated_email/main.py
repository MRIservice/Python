#!/usr/bin/python3

import os
from tkinter.font import names
import pandas
import smtplib
import random
import datetime as dt
# from datetime import datetime # This is the best method.

BIRTHDAYS = "birthdays.csv"
TXT_TO_STRIP = "[NAME]"
LETTER_DIR = "./letter_templates"

my_email = "name@KMyDomain.com"
my_password = "MyPassword"


# Create tupple of day to send a card

# today = (today_month, today_day)
now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv(BIRTHDAYS)  # CSV containing name , email and birthday

new_dict = {(data_row['month'], data_row['day'])
             : data_row for (index, data_row) in data.iterrows()}

# For Troubleshooting make sure CSV value is equl to the current date or this will not run
if today in new_dict:  # Today tupple ----- today = (month, day)
    letter_path = random.choice(os.listdir(LETTER_DIR))
    birthday_person = new_dict[today]

    with open(f"{LETTER_DIR}/{letter_path}") as letter_file:
        letter_contents = letter_file.read()
        # REPLACE MUST BE SAVED AS VARIABLE OR IT WILL NOT WORK
        new_letter = letter_contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("mail.mriservice.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="davidh@mriservice.com",
                                msg=f"Subject:Happy Birthday!\n\n{new_letter}")
