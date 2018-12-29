from flask import Flask, jsonify, request
import firebase_admin
import pyrebase
from flask_cors import CORS
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from RequestData import RequestData

# THIS is the magic. This local private file is what allows me to read and write to database
cred = credentials.Certificate("/users/ezraj/OneDrive/Documents/firebase/secret.json")

config = {
    "apiKey": "AIzaSyAnqidILVhAGjxg5Ya3AJhWtmGR5RvJCMY",
    "authDomain": "chemdata-a814d.firebaseapp.com",
    "databaseURL": "https://chemdata-a814d.firebaseio.com",
    "projectId": "chemdata-a814d",
    "storageBucket": "chemdata-a814d.appspot.com",
    "messagingSenderId": "219386075120"
}
firebase_admin.initialize_app(cred, {
    "apiKey": "AIzaSyAnqidILVhAGjxg5Ya3AJhWtmGR5RvJCMY",
    "authDomain": "chemdata-a814d.firebaseapp.com",
    "databaseURL": "https://chemdata-a814d.firebaseio.com",
    "projectId": "chemdata-a814d",
    "storageBucket": "chemdata-a814d.appspot.com",
    "messagingSenderId": "219386075120"
})

# this is a flask app
app = Flask(__name__)

#This will accept cors
CORS(app)

#for regulate login user
firebase = pyrebase.initialize_app(config)
user_db = firebase.database()
my_auth = firebase.auth()

token = ''


@app.route("/")
def hello():
    return jsonify({"about": "Hello World!"})


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    data = ''
    if request.method == 'POST':
        data = request.get_json()
        print(data)
    user = my_auth.sign_in_with_email_and_password(data['user'],
                                                   data['password'])  # need to use firebase.auth()
    global token
    token = user['idToken']
    return jsonify(user)


@app.route('/lab-one', methods=['GET', 'POST'])
def answer_one():
    data = ''

    print(token)
    decoded_token = auth.verify_id_token(token)
    isPost = False
    if request.method == 'POST':
        isPost = True
        data = jsonify(request.get_json())
        authenticated = db.reference("test").get()

    # parse into object

    # request proper lab
    # query_data = jsonify(lab_root.child(request_data.lab).get())

    return jsonify(authenticated)


if __name__ == "__main__":
    app.run()
