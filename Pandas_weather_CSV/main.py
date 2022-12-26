#!/usr/bin/python3
from multiprocessing import Condition
import pandas
#import csv

CSV = "weather_data.csv"

# with open(CSV) as weather_data:
#   data = csv.reader(weather_data)
#  temps = []

# pull title information, convert string > integer and put into list
#   for item in data:
#      if item[1] != "temp":
#         temps.append(int(item[1]))

data = pandas.read_csv(CSV)

# print(data["temp"])
# print(data.temp)

max_temp = data[data.temp == data.temp.max()]

monday = data[data.day == "Monday"]

temp_f = monday.temp * 9/5 + 32

print(monday)

print(max_temp)

print(monday.condition)

print(temp_f)

# print(fahrenheit)

# print(row.temp)
