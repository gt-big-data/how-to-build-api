from flask import Flask, request, jsonify
import json

app = Flask(__name__)

db = open("data.json") # Our adhoc database
data = json.load(db)
songs = data['songs']

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return jsonify({"Big Data": "The Big Picture"}) #Transforms data stored
    else:
        return "405: Restricted method"

@app.route("/songs", methods=['GET'])
def song():
    if request.method == 'GET':
        return jsonify(get_bus_data(songs)) #Transforms data stored
    else:
        return "405: Restricted method"

@app.route("/songs/<int:index>", methods=['GET'])
def getSongIndex(index):
    if request.method == 'GET':
        return jsonify(songs[index]) #Transforms data stored
    else:
        return "405: Restricted method"

if __name__ == "__main__":
    app.run()
