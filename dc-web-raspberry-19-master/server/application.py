# export FLASK_APP=application.py
# flask run --host=0.0.0.0
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

from blueprints.led_blueprint import bp_led
from blueprints.api_blueprint import bp_api
from temperature import sensor
from movement import Movement

app.register_blueprint(bp_led)
app.register_blueprint(bp_api)

@app.route('/')
def index():
    return render_template('index.html', sensor=sensor)

def movementDetected():
    socketio.emit('alert', 'Mouvement détecté', Broadcast=True)

movementSensor = Movement(17, detectFunction=movementDetected)
movementSensor.startDetection()

@app.route('/stop_detector')
def stopDetector():
    movementSensor.stopDetection()

@app.route('/start_detector')
def startDetector():
    movementSensor.startDetection()

    

# def message_loop():
#     while True:
#         message = input('Votre message ?')
#         socketio.emit('alert', message, Broadcast=True)

# # Vue que notre méthode pour lire nos message est une boucle infinie
# # Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# # Ici nous créons un Thread qui va permettre à notre fonction de se lancer 
# # en parallèle du serveur.
# read_messages = Thread(target=message_loop)
# read_messages.start()
