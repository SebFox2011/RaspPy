from flask import Blueprint, redirect, render_template, request, url_for,jsonify
from classes.temperature import Temperature

bp_api = Blueprint('api', __name__, url_prefix='/api')

temps = {
    'celsius' : 0,
    'fahrenheit' : 0
}

temp = Temperature ('28-01131a4f0da1')
temp.initialise()

@bp_api.route('/temperature', methods=["GET"])
def readTemp():
    temps ['celsius'] = temp.read_temp()
    temps['fahrenheit'] = temp.read_tempF()
    return jsonify(temps) 

