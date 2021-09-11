from flask import Flask, request, jsonify

import bot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/chat", methods=["POST"])
def chat():
    if request.method == "POST":

        request_data = request.get_json()

        message = request_data['message']

        status, response = bot.chat(message)

        data = {}

        if status == 0:

            data["reply"] = response

            data["status"] = 'Success'

            return jsonify(data)

        else:

            data["reply"] = response

            data["status"] = 'failed'

            return jsonify(data)



if __name__ == '__main__':
    app.run()
