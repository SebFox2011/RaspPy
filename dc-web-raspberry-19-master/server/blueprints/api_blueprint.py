from flask import Blueprint, redirect, url_for, jsonify
from temperature import sensor
from light import lightSensor
bp_api = Blueprint('api', __name__, url_prefix='/api')

@bp_api.route('/temperature')
def temperature_json():
    temp_c = sensor.read_temp()
    return jsonify({
        'temp': temp_c
    })

@bp_api.route('/light')
def light_json():
    light = lightSensor.read_light()
    return jsonify({
        'light': light
    })
