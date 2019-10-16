from flask import Blueprint, redirect, render_template, request, url_for,jsonify
from classes.temperature import Sensor
from classes.light import lightSensor

bp_api = Blueprint('api', __name__, url_prefix='/api')

temps = {
    'celsius' : 0,
    'fahrenheit' : 0
}

luminosite = {
    'day': ''
}


@bp_api.route('/temperature', methods=["GET"])
def readTemp():
    temps ['celsius'] = Sensor.read_temp()
    temps['fahrenheit'] = Sensor.read_tempF()
    return jsonify(temps) 


@bp_api.route('/luminosite', methods=["GET"])
def readlight():
    if lightSensor.read_light() > 150:
        luminosite['day'] = 'nuit'
    else:
        luminosite['day'] = 'jour'
    return jsonify(luminosite['day'])

