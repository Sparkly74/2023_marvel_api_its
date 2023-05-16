import hashlib # Importer la librairie pour générer un hash
import time # Importer la librairie pour générer un timestamp
import requests # importer al librairie requests pour faire des requêtes HTTP
from flask import Flask, jsonify # Importer la librairie Flask pour créer une API et jsonify pour retourner du JSON

app = Flask(__name__) # Créer une instance de l'application Flask
app.config.from_pyfile('config.py') # Chargez la configuration depuis le fichier config.py

PUBLIC_KEY = app.config['MARVEL_PUBLIC_KEY'] # Récupérer la clé publique depuis la configuration
PRIVATE_KEY = app.config['MARVEL_PRIVATE_KEY'] # Récupérer la clé publique depuis la configuration
BASE_URL = app.config['BASE_URL'] # Récupérer l'URL de base depuis la configuration config.py

def generate_hash(ts,private_key, public_key): # Définiri une fonction pour générer un hash
    m = hashlib.md5() # Créer une instance de l'algorithme MD5, SHA 256, SHA 512 ...
    m.update(f"{ts}{private_key}{public_key}".encode('utf-8')) # Mettre à jour le hash avec le timestamp, la clé privée et la clé publique
    return m.hexdigest() # Retourner le hash en hexadécimal

@app.route('/characters') # Création d'une route pour récupérer les personnages
def get_characters(): # Définir une fonction pour récupérer les personnages
    ts = str(time.time()) # Générer un timestamp
    hash = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY) # Générer un hash avec le timestamp, la clé privée et la clé publique
    params = { # Définir les paramètres de la requête sur la base d'un dictionnaire
        'apikey': PUBLIC_KEY,
        'ts' : ts,
        'hash' : hash,
        'limit' : 100
    }

    response = requests.get(f"{BASE_URL}characters", params=params) # Faire une requete HTTP GET sur l'URL de base + characters
    return jsonify(response.json()) # Retourner le JSON de la réponse

app.run(debug=True) # Lancer l'application en mode debug


