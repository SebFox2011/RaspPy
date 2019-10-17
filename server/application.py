from flask import Flask
from flask import render_template  # jinja2
from classes.temperature import Sensor
from classes.light import lightSensor
from classes.movement import Movement

from flask_socketio import SocketIO, send, emit
from threading import Thread

from blueprints.led_blueprint import bp_led
from blueprints.api_blueprint import bp_api

app = Flask(__name__)
app.register_blueprint(bp_led)
app.register_blueprint(bp_api)

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', temp=Sensor, luminosite=lightSensor)

if __name__ == '__main__':
    app.run()


def detectMovement():
    socketio.emit('alert', 'Mouvement détécté', Broadcast=True)

movementSensor = Movement(17, detectFunction=detectMovement)
movementSensor.startDetection()

@app.route('/stop_detector')
def stopDetector():
    movementSensor.stopDetection()

@app.route('/start_detector')
def startDetector():
    movementSensor.startDetection()

thread = movementSensor.startDetection()
##thread.join()

def message_loop():
    while True:
        message = input('Votre message ?')
        socketio.emit('alert', message, Broadcast=True)

# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer 
# en parallèle du serveur.
read_messages = Thread(target=message_loop)
read_messages.start()
