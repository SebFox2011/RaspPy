from flask import Blueprint, redirect, url_for
from led import Led
from GPIO import GPIO_initialize

bp_led = Blueprint('led', __name__, url_prefix='/led')

GPIO_initialize()

leds = {
    'red': Led(14),
    'blue': Led(15)
}
@bp_led.route('/on/<led_name>')
def led_on(led_name):
    leds[led_name].on()
    return redirect(url_for('index'))

@bp_led.route('/off/<led_name>')
def led_off(led_name):
    leds[led_name].off()
    return redirect(url_for('index'))

@bp_led.route('/blink/<led_name>')
def led_blink(led_name):
    leds[led_name].asyncBlink(10, 0.07)
    return redirect(url_for('index'))