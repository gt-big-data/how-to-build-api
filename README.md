# How To Build An API
![logo](https://drive.google.com/uc?id=1tsoEUqYWJoT_GNsRVhNlrF4rK1xZUqRz)
This talk was given on 2/7/2019. For supplementary information explaining the premise of an API, go [here](https://docs.google.com/presentation/d/1GwtD5kXjfVzrbJ6Uh2l4wQgwVe9uJNEcqiIKkpHqp1I/edit?usp=sharing)!

In this tutorial, we will be creating the API server for our version of Spotify! The data is a JSON array of multiple song objects with attributes: title, artist, year created, and album cover image url located in Google drive. The data looks like this:
```
{"songs":[
  {"title":"Favorite Song","artist":"Chance the Rapper","year":"2015","img_url":"https://drive.google.com/uc?id=1vwOMSjqkdeAl4Er0ETk_K9GR5IiyI0s4"},
  {"title":"SICKO MODE","artist":"Travis Scott","year":"2012","img_url":"https://drive.google.com/uc?id=13F_j2ilYn1sBpGdnKb3qbunle3b8KsBT"},
  ...
  {"title":"Stay","artist":"Post Malone","year":"2016","img_url":"https://drive.google.com/uc?id=1v0nFVnaA-RXHuGRgWo8_OSgzqqx6xbHJ"}
  ]
}
```
The Google Drive folder for all the album covers is found [here](https://drive.google.com/drive/folders/1l4MfN34ReJxN86WQvpKDbdCVZCw01cve?usp=sharing)!

## System Requirements

You will need Python >= 2.7 or Python >=3.4

You will also need the following packages: flask, flask_cors
```shell
pip install flask, flask_cors # Python 2

# or

python3 -m pip install flask, flask_cors # Python 3
```

## Instructions

### 1. Importing Flask
Create the file api/app.py

Add the following lines of code to the top of your file.
```python
from flask import Flask, request, jsonify
import json
```
The first line imports Flask framework.
The second line imports a library that parses JSON.

### 2. Allowing Flask to have execution priveleges
Add this line of code after your import statements.
```python
app = Flask(__name__)
```
It tells the flask server where it is in the directory so it has knowledge of where it's assets(the database) are.

### 3. Access our Database
After Step 2, add this:
```python
db = open("data.json") # Our adhoc database
data = json.load(db)
songs = data['songs']
```
This is NOT a database. To simplify the tutorial, we are using a JSON file to store our data. This is typically  not done in production.

Now for the fun stuff!

### 4. Adding Routes
Remember in the talk how we discussed routes in an API server.

Routes we will be making day:
  - http://localhost:5000/
  - http://localhost:5000/songs/
  - http://localhost:5000/songs/*

They are all GET methods that, if you recall, returns a payload in the response.

#### Index/Home Route "/"
```python
@app.route("/", methods=['GET']) # 1.
def index(): # METHOD
    if request.method == 'GET': # 3.
        return jsonify({"Big Data": "The Big Picture"}) # 4.
    else:
        return "405: Restricted method"
```
A lot going on in the same block. Let's walk through it!
1. This specifies the route we will use in the server. In this case ```"/"```

2. Each time an end user calls this route, we execute the method under the route. In this case ```index```

3. If this is a ```GET``` method, do something. In this case, return the JSON payload as a response.

4. Transforms the data to JSON.

#### Songs "/songs/"
```python
@app.route("/songs", methods=['GET'])
def song():
    if request.method == 'GET':
        return jsonify(songs) #Transforms data stored
    else:
        return "405: Restricted method"
```
Only thing that is different here is what we are returning. Instead of us fooling around, we are returning our ```songs``` as a payload in the response.

#### Specific Song "/songs/<:id>"
```python
@app.route("/songs/<int:index>", methods=['GET']) # int wildcard
def getSongIndex(index):
    if request.method == 'GET':
        return jsonify(songs[index]) #Transforms data stored
    else:
        return "405: Restricted method"
```
As you might imagine, we want to be able to dynamically ask our API for information without giving every single route a specific name. We denote ```<int:index>``` as the wildcard route to get a specific song on in songs using an ```int``` index.

And there you have it! Almost done.

### 5. Finishing Up
```python
if __name__ == "__main__":
    app.run()
```

Nothing much to this. This allows the server to be run only if you run it directly: ```python app.py```. Note ```__name__``` is the same name in Step 2.

If this were a library, and I tried importing app.py ```import app``` in another file, the server would not run.

## 6. Run it!

Youre DONE!

In api/ run API server
```shell
python app.py
```

To see the UI server the frontend team created for us, we need to do a couple of things!
We will add the following two lines to the top of our file:
```python
from flask import Flask, request, jsonify
import json
from flask_cors import CORS # **NEW**

app = Flask(__name__)
CORS(app) # **NEW**

```
This will allow your frontend server's JavaScript to talk to our API server we built. It will also allow us to retrieve the album cover images from our public Google Drive folder.


Now, in a separate Terminal/CMD window, go the top of the how-to-build-api/ directory and run this command:
```shell
python -m SimpleHTTPServer 80 # Python 2

# or  

python3 -m http.server 80 # Python 3
```

Now go to ```http://localhost:80``` in to your browser!
