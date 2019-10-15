import RPi.GPIO as GPIO  # bibliothèque pour utiliser les GPIO
import time              # bibliothèque pour gestion du temps
from threading import Thread

class Led:
    def __init__(self,numGPIO):
        self.numGPIO = numGPIO
        GPIO.setup(numGPIO,GPIO.OUT)  # la pin 18 réglée en sortie (output)

    def on(self):
        GPIO.output(self.numGPIO,GPIO.HIGH)   # sortie au niveau logique haut (3.3 V)

    def off(self):
        GPIO.output(self.numGPIO,GPIO.LOW)   # sortie au niveau logique haut (3.3 V)

    def blink(self, numBlink, sleepTime):
        i=0
        while i < numBlink:
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            i+=1

    def asyncBlink (self, numBlink, sleepTime):
        thread = Thread(target=self.blink, args=(numBlink,sleepTime))
        thread.start()
        return thread

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BCM)   # mode de numérotation des pins
        GPIO.setwarnings(False)

    @classmethod
    def  clean(cls):
        GPIO.cleanup()

def clignote():
    Led.initialize()
    greenLed = Led(18)
    redLed = Led(15)
    '''redLed.blink(10,0.25)
    greenLed.blink(50,0.05)'''
    redLed.asyncBlink(10,0.25)
    greenLed.asyncBlink(50,0.05)

    '''while True:     # boucle répétée jusqu'à l'interruption du programme
        greenLed.on()   # sortie au niveau logique haut (3.3 V)
        redLed.off()   # sortie au niveau logique bas (0 V)
        time.sleep(0.5)               # on ne change rien pendant 1 seconde
        greenLed.off()   # sortie au niveau logique bas (0 V)
        redLed.on()    # sortie au niveau logique haut (3.3 V)
        time.sleep(0.5)'''