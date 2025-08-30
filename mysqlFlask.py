import mysql.connector
from flask import Flask, request, jsonify 

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nitte.edu.in",
    database="alan"
)

cursor = db.cursor(dictionary=True)

@app.route('/users', methods=['GET','POST'])
def get_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

