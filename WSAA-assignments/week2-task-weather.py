#week 2 assignment - Current Weather

# python program call currentweather.py that prints out current temperature and wind direction only in current location
import requests
import json
from geopy.geocoders import Nominatim

#location to get results from
latitude = 52.27021579560998
longitude = -9.707456054277275

url = f"https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
response = requests.get(url)
#print(response.json())
data = response.json()
#with open ("currentweather.json", "w") as fp:
           #json.dump(data, fp)
           
temp = data["current_units"]
print("temperature_2m")


print("")