from flask import Flask, jsonify
from dotenv import load_dotenv
load_dotenv()
import os
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL config #
mysql = MySQL()
app.config['MYSQL_DATABASE_USER']     = os.getenv("DB_USER")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("DB_PASS")
app.config['MYSQL_DATABASE_DB']       = os.getenv("DB_NAME")
app.config['MYSQL_DATABASE_HOST']     = os.getenv("DB_HOST")
mysql.init_app(app)

@app.route("/")
def hello_world():
  x = {
    "message" : "Hello World",
    "code" : 200
  }
  return jsonify({"data": x})

@app.route("/api/register")
def register():
  return jsonify("register here")

@app.route("/api/login") # this is should POST method
def login():
  return jsonify("login here please!")

@app.route("/api/dbtest")
def get_db():
  try:
    conn  = mysql.connect()
    csr   = conn.cursor()
    csr.execute('SELECT * FROM customers')  # my own table
    data  = csr.fetchall()
    return jsonify(data)
  except:
    return jsonify("Can not find database")