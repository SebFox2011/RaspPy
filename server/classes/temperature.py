# Imports
import os
import glob
import time


class Temperature:
    def __init__(self,identifiant):
        self.online = True
        # Chemin du fichier contenant la température (remplacer par votre valeur trouvée précédemment)
        self.device_file = '/sys/bus/w1/devices/'+ str(identifiant) + '/w1_slave'

    # Une fonction qui lit dans le fichier température
    def read_temp_raw(self):
        try:
            f = open(self.device_file, 'r')  # Ouvre le fichier
            lines = f.readlines() # Returns the text
            f.close()
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
    # Lis la temperature Fahrentheit
    def read_tempF(self):
        tempF = self.read_temp()*9/5 + 32
        return round(tempF, 3)
    
    @classmethod
    def initialise(cls):
        # Intialisation des broches
        os.system('modprobe w1-gpio')  # Allume le module 1wire
        os.system('modprobe w1-therm')  # Allume le module Temperature
            
# On affiche la temérature tant que le script tourne
#while True:
    #print(temp.read_temp())
    #time.sleep(1)