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

