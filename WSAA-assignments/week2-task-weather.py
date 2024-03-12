#week 2 assignment - Current Weather

import requests
import json

#get specific location weather information via url
#current location
#longitude = 52.269379
#latitude = -9.702950
url = "https://api.open-meteo.com/v1/forecast?latitude=52.26&longitude=-9.7&current=temperature_2m,wind_speed_10m"
response = requests.get(url)

#write to new file
data = response.json()
with open("currentweather.json", "w") as fp:
    json.dump(data, fp)

#grab data to print
temperature = data["current"]["temperature_2m"]
windspeed = data["current"]["wind_speed_10m"]
print(f"the current temperature is: {temperature} degrees celcius")
print(f"The current wind speed is: {windspeed}mps")