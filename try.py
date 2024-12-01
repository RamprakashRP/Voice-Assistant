'''import webbrowser
import time
from time import sleep
import pyautogui
import os
from PyDictionary import PyDictionary
from googlesearch import search
import requests
import json

# Enter your API key here
api_key = "1a2c9e60c84cc2e572cd925c7a020db1"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
    '''
word = ["hi", "hello", "what", "The", "what is", "what is your"]

def comparewords(word1, word2):
    if word1 in word2:
        return word2
    elif word2 in word1:
        return word1

    if


comparewords("what", "What is This")

def checkword(words, query):
    c = 0
    inwords = []
    for i in words:
        if i in query:
            c += 1
            inwords.append(i)

    print(c)
    print(inwords)

    if c == 1:
        return true
    if c == 2:
        n = 0
        #for i in inwords:




h = "what is your name"

#print(checkword(word, h))
