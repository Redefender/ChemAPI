import pyrebase

config = {
    "apiKey": "AIzaSyAnqidILVhAGjxg5Ya3AJhWtmGR5RvJCMY",
    "authDomain": "chemdata-a814d.firebaseapp.com",
    "databaseURL": "https://chemdata-a814d.firebaseio.com",
    "projectId": "chemdata-a814d",
    "storageBucket": "chemdata-a814d.appspot.com",
    "messagingSenderId": "219386075120"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = input('Please enter your email\n')
password = input('Please enter your password\n')

# create new user
# user = auth.create_user_with_email_and_password(email, password)

# sign in
auth.sign_in_with_email_and_password(email, password)
