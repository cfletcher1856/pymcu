#!/usr/bin/env python

import  pywapi
import string
from pprint import pprint

zipcode = "78729"
noaa_station = "KAUS"

google_result = pywapi.get_weather_from_google(zipcode)
yahoo_result = pywapi.get_weather_from_yahoo(zipcode)
noaa_result = pywapi.get_weather_from_noaa(noaa_station)

google_forcast = google_result['forecast_information']
google_conditions = google_result['current_conditions']

google = "The condition in {0} at {1} is {2} with {3}, Temp: {4} F, and {5}"

print google.format(
    google_forcast['city'], google_forcast['current_date_time'],
    google_conditions['condition'], google_conditions['humidity'],
    google_conditions['temp_f'], google_conditions['wind_condition']
)
