import csv
from os import path

import requests

KEY_PATH = path.join('creds', 'darksky')
API_URL = 'https://api.forecast.io/forecast/{APIKEY}/{LATITUDE},{LONGITUDE},{TIME}'
OUTPUT_PATH = path.join('data', 'weather.csv')
MIN_YEAR = 2014
MAX_YEAR = 2016
MONTH = 4
MIN_DAY = 1
MAX_DAY = 30
LATITUDE = 47.6062
LONGITUDE = -122.3321

with open(KEY_PATH, 'r') as key_file:
    key = key_file.read().strip()

columns = ['year', 'day', 'hour', 'summary', 'temperature', 'windSpeed', 'precipIntensity']
with open(OUTPUT_PATH, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(columns)

    padded_month = str(MONTH).zfill(2)
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        for day in range(MIN_DAY, MAX_DAY + 1):
            padded_day = str(day).zfill(2)
            time_string = '{year}-{month}-{day}T12:00:00'.format(year=year, month=padded_month, day=padded_day)
            url = API_URL.format(APIKEY=key, LATITUDE=LATITUDE, LONGITUDE=LONGITUDE, TIME=time_string)
            resp = requests.get(url)
            hourly_data = resp.json()['hourly']['data']
            hourly_data.sort(key=lambda hour: hour['time'])

            for hour, datum in enumerate(hourly_data):
                row = [year, day, hour]
                for col in columns[3:]: # skip first 3 columns
                    if col in datum:
                        row.append(datum[col])
                    else:
                        row.append(None)
                writer.writerow(row)

            print('wrote rows for', year, day)
