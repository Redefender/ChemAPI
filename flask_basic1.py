from flask import Flask, jsonify, request
from collections import defaultdict
from flask_cors import CORS
import pyrebase

config = {
    "apikey": "AIzaSyAnqidILVhAGjxg5Ya3AJhWtmGR5RvJCMY",
    "authDomain": "chemdata-a814d.firebaseapp.com",
    "databaseURL": "https://chemdata-a814d.firebaseio.com",
    "projectId": "chemdata-a814d",
    "storageBucket": "chemdata-a814d.appspot.com",
    "messagingSenderId": "219386075120"
}

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return jsonify({"about": "Hello World!"})


@app.route('/lab-one', methods=['GET', 'POST'])
def answer_one():
    # if request.method == 'POST':
    # questions = request.json['questions']  # ex ['1','5','7']

    # convert all strings within question list to ints
    # questions = map(int, questions)

    # get the answers for each question (also a dictionary of lists) probably going to use mongodb or firebase
    test_answer = [
        {"This is NOT an answer, just to fix off by one errors"},
        {"answer": "this is the answer for question 1"},
        {"answer": "this is the answer for question 2"},
        {"answer": "this is the answer for question 3"},
        {"answer": "this is the answer for question 4"},
        {"answer": "this is the answer for question 5"},
        {"answer": "this is the answer for question 6"},
        {"answer": "this is the answer for question 7"},

    ]

    # create a dictionary of lists
    response_dictionary = defaultdict(list)

    # for i in questions:
    #     response_dictionary[i].append(test_answer[i])

    return jsonify({"lab": "Lab One", "answers": [
        {
            "answer": "2",
            "identifier": ".",
            "value": "question"
        },
        {
            "answer": "3",
            "identifier": ".",
            "value": "question"
        }
    ]})

if __name__ == "__main__":
    app.run()
