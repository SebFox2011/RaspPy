from flask import Blueprint, redirect, render_template, request, url_for
from classes.led import Led
from threading import Thread
from classes.GPIO import GPIO_initialize

bp_led = Blueprint('led', __name__, url_prefix='/led')
GPIO_initialize()

leds = {
    'red' : Led(15),
    'green' : Led(18)
}

@bp_led.route('/red', methods=["GET"])
def LedBlinkRed():
    leds['red'].asyncBlink(10,0.25)
    return redirect('/') 

@bp_led.route('/green', methods=["GET"])
def LedBlinkGreen():   
    leds['green'].asyncBlink(50,0.05)
    return redirect('/') 

@bp_led.route('/gr/on', methods=["GET"])
def LedGreenOn():   
    leds['green'].on()
    return redirect('/') 

@bp_led.route('/gr/off', methods=["GET"])
def LedGreenOff():   
    leds['green'].off()
    return redirect('/') 

@bp_led.route('/rd/on', methods=["GET"])
def LedRedOn():   
    leds['red'].on()
    return redirect('/') 

@bp_led.route('/rd/off', methods=["GET"])
def LedRedOff():   
    leds['red'].off()
    return redirect('/') 

# peut remplacer les 4 méthodes précédentes
@bp_led.route('/on/<ledColor>', methods=["GET"])
def on(ledColor):   
    leds[ledColor].on()
    return redirect('/') 

@bp_led.route('/off/<ledColor>', methods=["GET"])
def off(ledColor): 
    leds[ledColor].off()
    return redirect('/')