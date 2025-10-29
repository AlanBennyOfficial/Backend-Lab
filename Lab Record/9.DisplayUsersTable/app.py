# 9. develop a Flask web application that connects to a MySQL database using the Flask-MySQLdb extension.
#     i) Create an API endpoint /users that retrieves all rows from the users table.
#     ii) Display the query result in a tabular format using a Jinja template (users.html).

from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database configuration
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()

    return render_template("users.html", rows=rows, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)