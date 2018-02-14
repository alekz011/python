#! /usr/bin/python3

import json, requests, sys

# Compute location from command line argument
if len(sys.argv) < 2:
    print('Usage: get_Weather.py <location>')
    sys.exit()
location = ' '.join(sys.argv[1:])

#Download the JSON data from OpenWeathermap.org's API
url ='http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=5dccb441d78b27da8f9de804f02a3fac&?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
