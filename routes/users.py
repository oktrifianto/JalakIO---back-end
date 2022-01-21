from flask import Flask, Blueprint, jsonify
from config.database import mysql           # import from config/database.py

app_user = Flask(__name__)
app_user = Blueprint('app_user', __name__)

@app_user.route("/api/hello-user")
def hello_user():
  try:
    conn  = mysql.connect()
    csr   = conn.cursor()
    csr.execute('SELECT * FROM customers')
    data  = csr.fetchall()
    return jsonify(
      data=data,
      status=200
    )
  except:
    return jsonify(
      data=[],
      status=404
    )