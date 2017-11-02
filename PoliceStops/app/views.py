import flask
from flask import render_template, request
from app import app
#from viz import create_map


@app.route('/')
@app.route('/index')
def index():
    stop_date_MIN = request.args.get('stop_date_MIN', default=None, type=str)
    stop_date_MAX = request.args.get('stop_date_MAX', default=None, type=str)
    driver_gender = request.args.get('driver_gender', default=None, type=str)
    driver_age_MIN = request.args.get('driver_age_MIN', default=None, type=int)
    driver_age_MAX = request.args.get('driver_age_MAX', default=None, type=int)
    driver_race_TUPLE = request.args.getlist('driver_race_TUPLE', type=str)
    violation_TUPLE = request.args.getlist('violation_TUPLE', type=str)
    search_conducted = request.args.get('search_conducted', default=None, type=bool)
    search_type_TUPLE = request.args.get('search_type', default=None, type=tuple)
    stop_outcome_TUPLE = request.args.getlist('stop_outcome_TUPLE', type=str)
    officer_gender = request.args.get('officer_gender', default=None, type=str)
    officer_age_MIN = request.args.get('officer_age_MIN', default=None, type=int)
    officer_age_MAX = request.args.get('officer_age_MAX', default=None, type=int)
    officer_race_TUPLE = request.args.getlist('officer_race_TUPLE', type=str)
    officer_rank_TUPLE = request.args.getlist('officer_rank_TUPLE', type=str)
    out_of_state = request.args.get('out_of_state', default=None, type=bool)
    #return str(stop_date_MIN) + str(stop_date_MAX) + str(driver_gender) + str(driver_age_MIN) + str(driver_age_MAX) + \
    #    str(driver_race_TUPLE) + str(violation_TUPLE) + str(search_conducted) + str(search_type_TUPLE) + \
    #    str(stop_outcome_TUPLE) + str(officer_gender) + str(officer_age_MIN) + str(officer_age_MAX) + \
    #    str(officer_race_TUPLE) + str(officer_rank_TUPLE) + str(out_of_state)
    #create_map()
    return render_template('index.html')

@app.route('/results/map.html')
def show_map():
    return flask.send_file('/Users/duffrind/ncf/data/project1/police-traffic-stop-explorer/PoliceStops/app/results/map.html')
