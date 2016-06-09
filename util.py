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
combined_data = bike_data.merge(weather_data)
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

def human_time(year, day, hour, day_of_week):
    base = 'April {}, {}, {} ({})'
    dow = DAY_NAMES[day_of_week]
    hh = human_hour(hour)
    text = base.format(day, year, hh, dow)
    pad_day = str(day).zfill(2)
    pad_hour = str(hour).zfill(2)
    return '<a href="/timepoint/{}/{}">{}</a>|{}{}{}'.format(day, hour, text, year, pad_day, pad_hour)

def human_location(location):
    text = location_data[location]['name']
    return '<a href="/location/{}">{}</a>'.format(location, text)

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
            info[col] = wdf[col].iloc[0]

        bdf.sort_values('num_bikes', ascending=False, inplace=True)
        bdf.reset_index(inplace=True)
        for i, full_row in bdf.iterrows():
            human_name = human_location(full_row['location'])
            rows.append([i+1, human_name, full_row['num_bikes']])
            info['total'] += full_row['num_bikes']
        result['years'][year] = info, rows
    return result

def location(location_string):
    data = location_data[location_string].copy()
    data['years'] = {}
    ldf = combined_data[combined_data['location'] == location_string]
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        rows = []
        info = {'year': year, 'total': 0}
        ydf = ldf[ldf['year'] == year]
        ydf.sort_values(['day', 'hour'], inplace=True)
        for _, full_row in ydf.iterrows():
            time_string = human_time(year, full_row['day'], full_row['hour'], full_row['day_of_week'])
            rows.append([time_string, full_row['summary'], full_row['precipIntensity'], \
                         full_row['temperature'], full_row['windSpeed'], full_row['num_bikes']])
            info['total'] += full_row['num_bikes']
        data['years'][year] = info, rows
    return data

def query(time, rainy, windy, weektime):
    data = {'years': {}}
    df = combined_data
    parts = []

    if rainy == 'yes':
        df = df[df['precipIntensity'] > 0]
        parts.append('rainy')
    elif rainy == 'no':
        df = df[df['precipIntensity'] <= 0]
        parts.append('dry')

    if windy == 'yes':
        df = df[df['windSpeed'] > 5]
        parts.append('windy')
    elif windy == 'no':
        df = df[df['windSpeed'] <= 5]
        parts.append('calm')

    if weektime == 'weekend':
        df = df[df['day_of_week'] >= 5]
        parts.append('on the weekend')
    elif weektime == 'weekday':
        df = df[df['day_of_week'] <= 4]
        parts.append('on a weekday')

    if time == 'morning':
        df = df[df['hour'] >= 5][df['hour'] <= 10]
        parts.append('in the morning')
    elif time == 'midday':
        df = df[df['hour'] >= 11][df['hour'] <= 15]
        parts.append('around midday')
    elif time == 'evening':
        df = df[df['hour'] >= 15][df['hour'] <= 20]
        parts.append('in the evening')
    elif time == 'night':
        df = df[(df['hour'] >= 21) | (df['hour'] <= 4)] # somehow bitwise works??
        parts.append('at night')

    data['name'] = ', '.join(parts)

    for year in range(MIN_YEAR, MAX_YEAR + 1):
        rows = []
        info = {'year': year, 'total': 0}
        ydf = df[df['year'] == year]
        ydf.sort_values(['day', 'hour'], inplace=True)
        for _, full_row in ydf.iterrows():
            time_string = human_time(year, full_row['day'], full_row['hour'], full_row['day_of_week'])
            location_name = human_location(full_row['location'])
            rows.append([time_string, location_name, full_row['summary'], full_row['precipIntensity'], \
                         full_row['temperature'], full_row['windSpeed'], full_row['num_bikes']])
            info['total'] += full_row['num_bikes']
        data['years'][year] = info, rows
    return data

def raw_locations():
    return location_data

def named_hours():
    result = []
    for hour in range(24):
        result.append((hour, human_hour(hour)))
    return result
