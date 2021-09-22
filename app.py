from flask import Flask, request, jsonify
import bot
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app, resources={r"*": {"origins": "*"}})
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#app.config['CORS_HEADERS'] = 'Content-Type'

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
