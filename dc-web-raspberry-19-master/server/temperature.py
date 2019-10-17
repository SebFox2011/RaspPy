# Imports
import os
import glob
import time

class TemperatureSensor:

    def __init__(self, sensor_name):
        self.online = True
        self.device_file = '/sys/bus/w1/devices/'+ sensor_name +'/w1_slave'

    # Une fonction qui lit dans le fichier température
    def read_temp_raw(self):
        try:
            f = open(self.device_file, 'r')  # Ouvre le dichier
            lines = f.readlines() # Returns the text
            f.close()
            self.online = True
            return lines
        except:
            self.online = False
            return ['', '']
        
    # Lis la temperature 
    def read_temp(self):
        lines = self.read_temp_raw()  # Lit le fichier de température
        if not self.online: # On vérifie que le capteur est bien branché, sinon on ne bloque pas la fonction.
            return 0
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        # On relis ensuite le fichier
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

    def read_temp_f(self):
        temp_c = self.read_temp()
        temp_f = (temp_c * 9 / 5) + 32
        return temp_f

    @classmethod
    def initialize(cls):
        # Intialisation des broches
        os.system('modprobe w1-gpio')  # Allume le module 1wire
        os.system('modprobe w1-therm')  # Allume le module Temperature
        
# On affiche la temérature tant que le script tourne
TemperatureSensor.initialize()

sensor = TemperatureSensor('28-01131b764e06')
# sensor2 = TemperatureSensor('28-01131a3eb0d1')

# while True:
#     print('Température Capteur 1 : ' + str(sensor1.read_temp()))
#     print('Température Capteur 2 : ' + str(sensor2.read_temp()))
#     time.sleep(1)
