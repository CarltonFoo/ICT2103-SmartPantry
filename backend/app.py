from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
import sys

# Create an application instance
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

# Define a route to fetch the avaialable articles
@app.route("/allarticles", methods=["GET"], strict_slashes=False)
def articles():
	if request.method == "GET":
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM flask.articles")
		columns = cur.description 
		result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
		mysql.connection.commit()
		cur.close()
		return jsonify(result)

# def articles():
# 	if request.method == "POST":
# 		details = request.form
# 		firstName = details['fname']
# 		lastName = details['lname']
# 		cur = mysql.connection.cursor()
# 		result = cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
# 		mysql.connection.commit()
# 		cur.close()
# 		return jsonify(result)

if __name__ == "__main__":
	app.run(debug=True)