from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"about":"Hello World!"})

@app.route('/one')
def first():
    return jsonify({"hit": "hit one"})
@app.route('/one/<float:num>', methods=['GET'])
def answer_one(num):
    number = str(num)
    return jsonify({'result': "answer to one with input " + number})

if __name__ == "__main__":
    app.run()