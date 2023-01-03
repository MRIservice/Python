#!/usr/bin/python3

import smtplib
import random
import datetime as dt

QUOTES = "quotes.txt"
quote_list = []

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 2:

    with open(QUOTES, "r") as quotes:
        for quote in quotes:
            quote_list.append(quote)

    rand_quote = random.choice(quote_list)

    # quote_list.readlines()  # is a better way to read lines of test


    # Note: For many reasons email is often hard to send to the recipient
    # It is often best to use smtp.gmail.com or other known server to send

    my_email = "davidh@rip1.com"
    my_password = "Palm2Squit1"

    with smtplib.SMTP("mail.mriservice.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="davidh@mriservice.com",
                            msg=f"Subject:New Quote of the Day\n\n{rand_quote}")

####################################################################################


# now = dt.datetime.now()
# year = now.year
# DayOfWeek = now.weekday()

# BirthDay = dt.datetime(year=1964, month=5, day=19, hour=9)
# print(BirthDay)
