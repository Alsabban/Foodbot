#import MySQL as MySQL
from flask_mysqldb import MySQL
from flask import Flask, request, jsonify

import bot

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MySQL_DB']='chatbot'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    fetcedata = cur.fetchall()
    cur.close()

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
