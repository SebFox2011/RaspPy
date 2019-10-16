from flask import Flask
from flask import render_template  # jinja2
from classes.temperature import Sensor
from classes.light import lightSensor

from blueprints.led_blueprint import bp_led
from blueprints.api_blueprint import bp_api

app = Flask(__name__)
app.register_blueprint(bp_led)
app.register_blueprint(bp_api)

@app.route('/')
def index():
    return render_template('index.html', temp=Sensor, luminosite=lightSensor)

if __name__ == '__main__':
    app.run()
