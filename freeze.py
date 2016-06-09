from flask_frozen import Freezer

from app import app
import util

freezer = Freezer(app)

@freezer.register_generator
def timepoint():
    for day in range(1, 31):
        for hour in range(24):
            yield{'day': day, 'hour': hour}

@freezer.register_generator
def location():
    for loc_name in util.raw_locations():
        yield {'location_string': loc_name}

@freezer.register_generator
def query():
    for time in ['morning', 'midday', 'evening', 'night', 'any']:
        for weektime in ['weekday', 'weekend', 'any']:
            for rainy in ['yes', 'no', 'any']:
                for windy in ['yes', 'no', 'any']:
                    yield {'params': '-'.join([time, weektime, rainy, windy])}

if __name__ == '__main__':
    freezer.freeze()
