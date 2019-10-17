import RPi.GPIO as GPIO
from led import Led
from GPIO import GPIO_initialize
import time
from threading import Thread

class Movement:

    def __init__(self, numGPIO, detectFunction = None, readyFunction = None):
        self.numGPIO = numGPIO
        GPIO.setup(self.numGPIO, GPIO.IN)
        self.running = False
        self.detectFunction = detectFunction
        self.readyFunction = readyFunction

    def detect(self):
        currentstate = 0
        previousstate = 0
        while self.running:
            # Lecture du capteur
            currentstate = GPIO.input(self.numGPIO)
            # Si le capteur est déclenché
            if currentstate == 1 and previousstate == 0:
                print("    Mouvement détecté !")
                if not (self.detectFunction is None):
                    self.detectFunction()
                # En enregistrer l'état
                previousstate = 1
            # Si le capteur est s'est stabilisé
            elif currentstate == 0 and previousstate == 1:
                print("    Prêt")
                if not (self.readyFunction is None):
                    self.readyFunction()
                previousstate = 0
            # On attends 10ms
            time.sleep(0.01)

    def startDetection(self):
        self.running = True
        thread = Thread(target=self.detect)
        thread.start()
        return thread

    def stopDetection(self):
        self.running = False

# GPIO_initialize()

# led = Led(15)

# def detectMovement():
#     led.asyncBlink(5, 0.10)

# movementSensor = Movement(17, detectFunction=detectMovement)
# thread = movementSensor.startDetection()
# thread.join()
