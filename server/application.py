from flask import Flask
from flask import render_template  # jinja2
from classes.temperature import Temperature

from blueprints.led_blueprint import bp_led

app = Flask(__name__)
app.register_blueprint(bp_led)

temp = Temperature ('28-01131a4f0da1')
temp.initialise()

@app.route('/')
def index():
    return render_template('index.html', temp=temp)

if __name__ == '__main__':
    app.run()
