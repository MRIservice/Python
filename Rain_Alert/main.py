#!/usr/bin/python3

import smtplib
import requests
import smtplib

my_email = "NAME@MyDomain.com"
my_password = "PASSWORD"

message = "It will rain today so grab a jacket"

# https://api.openweathermap.org/data/2.5/onecall?lat=29.651634&lon=-82.324829&appid=c465bae37be05835eb0e4e223101ed3f

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR_API_KEY"

my_lat = 29.651634
my_lon = -82.324829

weather_parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "curent,minutely,daily",
}

api_call = "https://api.openweathermap.org/data/2.5/onecall?lat = my_lat & lon = my_lon & appid = c465bae37be05835eb0e4e223101ed3f"

response = requests.get(api_endpoint, params=weather_parameters)

response.raise_for_status()

weather_data = response.json()

# weather_code = weather_data['hourly'][0]["weather"][0]["id"]

rain = False

weather_slice = weather_data['hourly'][:12]  # slice provides 12 hours
for hour in weather_slice:
    weather_code = hour["weather"][0]["id"]
    if int(weather_code) <= 700:
        rain = True

if rain:
    with smtplib.SMTP("mail.mriservice.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="davidh@mriservice.com",
                            msg=f"Subject:Rain Today!\n\n{message}")
    
