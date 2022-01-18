from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route("/api/login")
def login():
  return jsonify("login here please!")