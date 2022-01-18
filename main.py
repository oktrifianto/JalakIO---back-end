from flask import Flask, jsonify
# import json

app = Flask(__name__)

class User:
  def login():
    return "nothing"

@app.route("/")
def hello_world():
  x = {
    "message" : "Hello World",
    "code" : 200
  }
  # return json.dumps(x)
  return jsonify({"data": x})

@app.route("/api/register")
def register():
  return jsonify("register here")

@app.route("/api/login")
def login():
  return jsonify("login here please!")