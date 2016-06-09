from flask import Flask, render_template, request

import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', locations=util.raw_locations(), days=range(1,31), hours=util.named_hours())

@app.route('/timepoint/<day>/<hour>')
def timepoint(day, hour):
    day = int(day)
    hour = int(hour)
    data = util.timepoint(day, hour)
    return render_template('timepoint.html', data=data)

@app.route('/location/<location_string>')
def location(location_string):
    data = util.location(location_string)
    return render_template('location.html', data=data)

@app.route('/query')
def query():
    time = request.args.get('time') or ''
    rainy = request.args.get('rainy') or ''
    windy = request.args.get('windy') or ''
    weektime = request.args.get('weektime') or ''
    data = util.query(time, rainy, windy, weektime)
    return render_template('query.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
