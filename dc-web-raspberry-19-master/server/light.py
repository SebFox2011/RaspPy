import RPi.GPIO as GPIO
from GPIO import GPIO_initialize
import time

class LightSensor:

    def __init__(self, numGPIO):
        self.numGPIO = numGPIO

    def read_light(self):
        lightCount = 0 #intitialisation de la variable de lumière
        GPIO.setup(self.numGPIO, GPIO.OUT)
        GPIO.output(self.numGPIO, GPIO.LOW)
        time.sleep(0.1) # on draine la charge du condensateur
        GPIO.setup(self.numGPIO, GPIO.IN)
        #Tant que la broche lit ‘off’ on incrémente notre variable
        while (GPIO.input(self.numGPIO) == GPIO.LOW):
            lightCount += 1
        return lightCount


GPIO_initialize()

lightSensor = LightSensor(27)
# Boucle infini jusqu'à CTRL-C
# while True:
#     print(lightSensor.read_light())
#     time.sleep(1)