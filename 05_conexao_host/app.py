import flask
from flask import request, json, jsonify
import requests
import flask_mysqldb
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "eunaosei"
app.config["MYSQL_DB"] = "flaskhost"

@app.route('/', methods=["GET"])
def index():
	data = requests.get('https://randomuser.me/api')
	return data.json()

@app.route('/inserthost', methods=["POST"])
def inserthost():
	data = requests.get("https://randomuser.me/api").json()
	username = data["results"][0]["login"]["username"]

	cur = mysql.connection.cursor()
	cur.execute("""INSERT INTO users(username) VALUES(%s)""", (username,))
	mysql.connection.commit()
	cur.close()

	return username

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port="5000")