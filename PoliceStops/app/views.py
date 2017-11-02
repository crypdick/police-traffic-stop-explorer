import flask
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/maps/map.html')
def show_map():
    return flask.send_file('/Users/duffrind/ncf/data/project1/PoliceStops/app/maps/map.html')
