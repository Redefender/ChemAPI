import pyrebase
import firebase_admin
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db


# THIS is the magic. This local private file is what allows me to read and write to database
cred = credentials.Certificate("/users/ezraj/OneDrive/Documents/firebase/secret.json")

firebase_admin.initialize_app(cred, {
    "apiKey": "AIzaSyAnqidILVhAGjxg5Ya3AJhWtmGR5RvJCMY",
    "authDomain": "chemdata-a814d.firebaseapp.com",
    "databaseURL": "https://chemdata-a814d.firebaseio.com",
    "projectId": "chemdata-a814d",
    "storageBucket": "chemdata-a814d.appspot.com",
    "messagingSenderId": "219386075120"
})

# auth = firebase.auth()
ref = db.reference('boi').set("this is a new test with admin")



