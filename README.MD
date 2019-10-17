# Projet python et Raspberry

## INstallation
dans VS Code ajouter le plugin sftp 
shift command + P > selectionner sft config et renseigner les champs

{
    "name": "Raspberry",
    "host": "10.23.161.7",
    "protocol": "sftp",
    "port": 22,
    "username": "pi",
    "password": "raspberry",
    "remotePath": "/home/pi/Documents/pyProj",
    "uploadOnSave": true
}

Sur le raspberry installer venv
sudo apt-get install python3-venv

activation de venv
python3 -m venv venv
. venv/bin/activate

INstaller Flask
pip install Flask

## Configuration

export FLASK_APP=application.py
flask run --host=0.0.0.0

## Capteur de température
https://raspberry-pi.developpez.com/cours-tutoriels/capteur/mag-pi-utiliser-port-gpio/partie-2-detection-temperature-1-wire/
https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf

s'assurer que le script suivant est bien installé sur le raspberry:

#!/bin/sh
if ! [ $(id -u) = 0 ]; then
   echo "Ce script doit être éxécuter en tant que root, utilisez la commande sudo pour éxécuter ce script. "
   exit 1
fi
echo "dtoverlay=w1-gpio" | tee -a /boot/config.txt
echo "wire" | tee -a /etc/modules
echo "w1-gpio" | tee -a /etc/modules
echo "w1-therm" | tee -a /etc/modules
echo "1wire activé ! (au prochain reboot) "

exécuter ensuite les commandes suivantes
nano 1-wire.sh
chmod u+x 1-wire.sh 
sudo ./1-wire.sh

## Modifier la config wifi sur raspi 0

créer un fichier  wpa_supplicant.conf

country=fr
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
 scan_ssid=1
 ssid="Digital2"
 psk="DIGITAL2015"
}

Le copier à la racine de la carte

## Utilisation de socket io

pip install flask-socketio