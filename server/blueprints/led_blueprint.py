from flask import Blueprint, redirect, render_template, request, url_for
from classes.led import Led
from threading import Thread

bp_led = Blueprint('led', __name__, url_prefix='/led')
Led.initialize()
@bp_led.route('/red', methods=["GET"])
def LedBlinkRed():
    redLed = Led(15)
    redLed.asyncBlink(10,0.25)
    return redirect('/') 

@bp_led.route('/green', methods=["GET"])
def LedBlinkGreen():   
    greenLed = Led(18)
    greenLed.asyncBlink(50,0.05)
    return redirect('/') 

@bp_led.route('/gr/on', methods=["GET"])
def LedGreenOn():   
    greenLed = Led(18)
    greenLed.on()
    return redirect('/') 

@bp_led.route('/gr/off', methods=["GET"])
def LedGreenOff():   
    greenLed = Led(18)
    greenLed.off()
    return redirect('/') 

@bp_led.route('/rd/on', methods=["GET"])
def LedRedOn():   
    redLed = Led(15)
    redLed.on()
    return redirect('/') 

@bp_led.route('/rd/off', methods=["GET"])
def LedRedOff():   
    redLed = Led(15)
    redLed.off()
    return redirect('/') 

# peut remplacer les 4 méthodes précédentes
@bp_led.route('/on/<int:ledPin>', methods=["GET"])
def on(ledPin):   
    redLed = Led(ledPin)
    redLed.on()
    return redirect('/') 

@bp_led.route('/off/<int:ledPin>', methods=["GET"])
def off(ledPin): 
    redLed = Led(ledPin)
    redLed.off()
    
    return redirect('/') 