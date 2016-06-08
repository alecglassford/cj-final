from glob import glob
from os import path

import pandas as pd

raw_data_path = path.join('raw_data', '*')
output_path = path.join('data', 'bikes.csv')

outputs = []
for filename in glob(raw_data_path):
    location = path.splitext(path.basename(filename))[0]
    df = pd.read_csv(filename, parse_dates=[0]) # Date is first col

    odf = pd.DataFrame()
    odf['year'] = df['Date'].apply(lambda date: date.year)
    odf['day'] = df['Date'].apply(lambda date: date.day)
    odf['hour'] = df['Date'].apply(lambda date: date.hour)
    odf['day_of_week'] = df['Date'].apply(lambda date: date.dayofweek)
    odf['location'] = location
    odf['num_bikes'] = df[df.columns[-1]] + df[df.columns[-2]] # total bikes (don't include pedestrians when distinguishable)

    # Conveniently the last 2 columns always sum to what we want, so can skip stuff below

    # if 'Fremont' in location:
    #     odf['num_bikes'] = df['Fremont Bridge West Sidewalk'] + df['Fremont Bridge East Sidewalk']
    # elif 'Burke' in location or 'Elliott' in location:
    #     odf['num_bikes'] = df['Bike North'] + df['Bike South']
    # elif 'MTS' in location:
    #     odf['num_bikes'] = df['Bike East'] + df['Bike West']
    # else:
    #     odf['num_bikes'] = df[df.columns[1]] # total number of bikes (+ pededstrians in a couple of cases)

    outputs.append(odf)
    print('processed', filename)

result = pd.concat(outputs)
result = result.fillna(-1) # there are a couple of gaps :(
result['num_bikes'] = result['num_bikes'].astype(int)
result.to_csv(output_path, index=False)
