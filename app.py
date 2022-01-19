from flask import Flask, jsonify, request
from dotenv import load_dotenv
load_dotenv()
import os
from flaskext.mysql import MySQL
from markupsafe import escape

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

@app.route("/api/register", methods = ['POST', "GET"])
def register():
  if request.method == 'GET':
    return jsonify("get register")

  if request.method == 'POST':
    """
    New user will register here
    * submit json data (example) @via CURL
      {
          "firstname" : "John",
          "email"     : "john@email.com"
      }
    """
    data    = request.get_json(force=True)
    email   = data['email']
    fsname  = data['firstname']
    return fsname
    # return jsonify('it is post method')

@app.route("/api/login") # this is should POST method
def login():
  return jsonify("login here please!")

@app.route("/api/user")
def show_users():
  try:
    conn  = mysql.connect()
    csr   = conn.cursor()
    query = 'SELECT * FROM customers'  # my own table
    csr.execute(query) 
    data  = csr.fetchall()
    return jsonify(
      data=data
    )
  except:
    return jsonify("Can not find database")

@app.route("/api/user/<username>")
def show_single_user(username):
  try:
    conn  = mysql.connect()
    csr   = conn.cursor()
    query = f'SELECT * FROM customers WHERE name="{escape(username)}"'
    count = csr.execute(query) # done
    # print(count)    # debug only
    data  = csr.fetchall()
    if count > 0:
      return jsonify(
        data=data
      )
    else: 
      return jsonify({"data : [name not found]"})
  except:
    return jsonify("db not found")


@app.route("/api/db-products")
def get_products():
  try:
    conn  = mysql.connect()
    csr   = conn.cursor()
    csr.execute('SELECT * FROM products')
    data  = csr.fetchall()
    return jsonify(f"data : {data}")
  except:
    return jsonify('data : 404')