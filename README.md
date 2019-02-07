# How To Build An API

This talk was given on 2/7/2019. For supplementary information, go [here](https://docs.google.com/presentation/d/1GwtD5kXjfVzrbJ6Uh2l4wQgwVe9uJNEcqiIKkpHqp1I/edit?usp=sharing)!

## System Requirements

You will need Python >= 2.7

You will also need the following package: flask
```shell
pip install flask
```

## Instructions

### 1. Importing Flask
Go to server/app.py

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

To see the UI, in a separate terminal/CMD window, in top of the directory run this command
```shell
python2 -m SimpleHTTPServer 8000
```

Now go to ```localhost:8000/```!
