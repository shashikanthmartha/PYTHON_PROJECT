from flask import Flask,request,jsonify
from flask_bcrypt import Bcrypt
form flask_mysqldb import MySQL

app = Flask(__name__)
bcrypt =Bcrypt(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL-PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'user_registration'
mysql = MySQL(app)

@app.route('/register', methods=['post'])
def register():
    data = request.get_json()
    username =data['username']
    email = data['email']
    password = data['password']

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    cur =mysql.connection.cursor()
    cur.excute("INSERT INTO users (username, email, password) VALUES (%s, %s %s)",(username, email, hashed_password_password))
    mysql.connection.commit()
    cur.close()

    return jsonify(message='User registered successfully'), 201

if __name__ == '__main__':
    app.run(debug=True)

