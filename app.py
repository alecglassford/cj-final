from flask import Flask, render_template

import util

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/timepoint/<day>/<hour>')
def timepoint(day, hour):
    day = int(day)
    hour = int(hour)
    data = util.timepoint(day, hour)
    return render_template('timepoint.html', data=data)

@app.route('/location/<location>')
def location(location):
    return location

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
