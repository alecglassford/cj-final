from glob import glob
from os import path
import json

raw_data_path = path.join('raw_data', '*')
output_path = path.join('data', 'locations.json')

result = {}
for filename in glob(raw_data_path):
    location = path.splitext(path.basename(filename))[0]
    name = location.replace('_', ' ')
    # This part is by hand ..
    coords = input('Lat,Long for {}? '.format(name))
    latitude, longitude = map(lambda c: float(c), coords.split(','))
    result[location] = {'name': name, 'latitude': latitude, 'longitude': longitude}

with open(output_path, 'w') as output_file:
    json.dump(result, output_file, sort_keys=True, indent=4)
