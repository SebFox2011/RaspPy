from flask import Flask
from flask import render_template  # jinja2

from blueprints.led_blueprint import bp_led

app = Flask(__name__)
app.register_blueprint(bp_led)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
