from flask import Flask, jsonify, request
from collections import defaultdict

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"about": "Hello World!"})


@app.route('/lab-one', methods=['GET', 'POST'])
def answer_one():
    questions = request.json['questions']  # ex ['1','5','7']

    # convert all strings within question list to ints
    questions = map(int, questions)

    # get the answers for each question (also a dictionary of lists) probably going to use mongodb or firebase
    test_answer = [
                   "This is NOT an answer, just to fix off by one errors",
                   "this is the answer for question 1",
                   "this is the answer for question 2",
                   "this is the answer for question 3",
                   "this is the answer for question 4",
                   "this is the answer for question 5",
                   "this is the answer for question 6",
                   "this is the answer for question 7",
                   "this is the answer for question 8",
                   "this is the answer for question 9",
                   "this is the answer for question 10"
                   ]

    # create a dictionary of lists
    response_dictionary = defaultdict(list)

    for i in questions:
        response_dictionary[i].append(test_answer[i])

    return jsonify(response_dictionary)


if __name__ == "__main__":
    app.run()
