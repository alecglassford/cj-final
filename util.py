from glob import glob
import json
from os import path

import pandas as pd

MIN_YEAR = 2014
MAX_YEAR = 2016
DAY_NAMES = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
             4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

bike_data_path = path.join('data', 'bikes.csv')
weather_data_path = path.join('data', 'weather.csv')
location_data_path = path.join('data', 'locations.json')

bike_data = pd.read_csv(bike_data_path)
weather_data = pd.read_csv(weather_data_path)
with open(location_data_path, 'r') as location_file:
    location_data = json.load(location_file)

def filter_time(df, year, day, hour):
    df = df[df['year'] == year][df['day'] == day][df['hour'] == hour]
    return df

def human_hour(hour):
    if hour == 0:
        return '12 a.m.'
    if hour <= 11:
        return str(hour) + ' a.m.'
    if hour == 12:
        return '12 p.m.'
    if hour <= 23:
        return str(hour - 12) + ' p.m.'
    raise Exception

timepoint_url = '/timepoint/{}/{}'
def nextDay(day, hour):
    return timepoint_url.format(day % 30 + 1, hour)
def prevDay(day, hour):
    if day == 1: return timepoint_url.format(30, hour)
    return timepoint_url.format(day - 1, hour)
def nextHour(day, hour):
    if hour == 23: return nextDay(day, 0)
    return timepoint_url.format(day, hour + 1)
def prevHour(day, hour):
    if hour == 0: return prevDay(day, 23)
    return timepoint_url.format(day, hour - 1)

def bg_color(hour):
    opacity = (1 + abs(hour - 12)) / 13.0
    return 'rgba(102, 102, 255, {}'.format(opacity)

def timepoint(day, hour):
    """
    Returns
    """
    result = {'day': day,
              'hour': human_hour(hour),
              'bg_color': bg_color(hour),
              'nextDay': nextDay(day, hour),
              'nextHour': nextHour(day, hour),
              'prevDay': prevDay(day, hour),
              'prevHour': prevHour(day, hour),
              'years': {}}
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        rows = []
        info = {'year': year, 'day': day, 'hour': human_hour(hour), 'total': 0}
        bdf = filter_time(bike_data, year, day, hour)
        wdf = filter_time(weather_data, year, day, hour)
        assert(len(wdf) == 1)

        info['day_of_week'] = DAY_NAMES[bdf['day_of_week'].iloc[0]]
        for col in wdf.columns[3:]:
            print(col, type(wdf[col].iloc[0]))
            info[col] = wdf[col].iloc[0]

        bdf.sort_values('num_bikes', ascending=False, inplace=True)
        bdf.reset_index(inplace=True)
        for i, full_row in bdf.iterrows():
            human_name = location_data[full_row['location']]['name']
            rows.append([i+1, human_name, full_row['num_bikes']])
            info['total'] += full_row['num_bikes']
        result['years'][year] = info, rows
    return result
