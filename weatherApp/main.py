import datetime as dt
import requests
import config

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

try:

    #prompts user to enter city
    CITY = input("Enter City:")

    url = BASE_URL + "appid=" + config.api_key + "&q=" + CITY

    response = requests.get(url).json()

    def kel_to_c_f(kelvin): #converts kelvin to c or f 
        celsius = kelvin - 273.15
        fehrenheit = celsius * (9/5) +32
        return celsius, fehrenheit


#gets the results from the api

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fehrenheit = kel_to_c_f(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_c, feels_life_f = kel_to_c_f(feels_like_kelvin)

    humidity = response['main']['humidity']

    description = response['weather'][0]['description']

    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

    wind_speed = response['wind']['speed']



#ask for user input
    val = input("Type C for Celsius or F for Fehrenheit")
    print(val)

    if val in ['C', 'c', 'Celsius', 'celsius']:
        temp = temp_celsius
        symbol = '°C'
    elif val in ['F', 'f', 'Fehrenheit', 'fehrenheit']:
        temp = temp_fehrenheit
        symbol = '°F'
    else:
        print("Invalid Input")
        exit()



#print results to stdout
    print(f"Weather in {CITY}: {description}")
    print(f"Temperature in {CITY}: {temp:.2f}{symbol}")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"Wind Speed in {CITY}: {wind_speed}m/s")


#catches error is invalid city is entered
except:
    print("ERROR: CITY NOT FOUND")










