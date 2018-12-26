from flask import Flask, jsonify, request
from collections import defaultdict
import firebase_admin
from flask_cors import CORS
import pyrebase
from firebase_admin import credentials
from firebase_admin import db
from RequestData import RequestData

cred = credentials.Certificate("/users/ezraj/OneDrive/Documents/firebase/secret.json")

firebase_admin.initialize_app(cred, {
    "apiKey": "AIzaSyAnqidILVhAGjxg5Ya3AJhWtmGR5RvJCMY",
    "authDomain": "chemdata-a814d.firebaseapp.com",
    "databaseURL": "https://chemdata-a814d.firebaseio.com",
    "projectId": "chemdata-a814d",
    "storageBucket": "chemdata-a814d.appspot.com",
    "messagingSenderId": "219386075120"
})

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return jsonify({"about": "Hello World!"})


@app.route('/lab-one', methods=['GET', 'POST'])
def answer_one():
    if request.data == 'POST':
        data = request.get_json()

    # parse into object
    request_data = RequestData("one", "two", "3")

    # request proper lab
    root = db.reference()
    query_data = root.child("4").get()

    return query_data


if __name__ == "__main__":
    app.run()
