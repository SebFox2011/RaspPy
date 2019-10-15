import RPi.GPIO as GPIO  # bibliothèque pour utiliser les GPIO
import time              # bibliothèque pour gestion du temps

GPIO.setmode(GPIO.BCM)   # mode de numérotation des pins
GPIO.setup(18,GPIO.OUT)  # la pin 18 réglée en sortie (output)
GPIO.setup(15,GPIO.OUT)  # la pin 18 réglée en sortie (output)

def clignote():
    while True:     # boucle répétée jusqu'à l'interruption du programme
        GPIO.output(18,GPIO.HIGH)   # sortie au niveau logique haut (3.3 V)
        GPIO.output(15,GPIO.LOW)   # sortie au niveau logique haut (3.3 V)
        time.sleep(0.5)               # on ne change rien pendant 1 seconde
        GPIO.output(18,GPIO.LOW)    # sortie au niveau logique bas (0 V)
        GPIO.output(15,GPIO.HIGH)    # sortie au niveau logique bas (0 V)
        time.sleep(0.5)