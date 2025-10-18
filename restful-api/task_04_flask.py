#!/usr/bin/python3
"""
provides a simple API using Flask.
"""

from flask import Flask
from flask import jsonify
from flask import request


# create web server
app = Flask(__name__)


@app.route("/")
def home():
    """
    define static route for root URL
    returns welcome string.
    """
    return ("Welcome to the Flask API!")


@app.route("/data")
def data():
    """
    define static route for /data endpoint
    returns list of all usernames stored in API.
    """
    formatted_list = []
    for key in users:
        formatted_list.append(key)
    return jsonify(formatted_list)


@app.route("/status")
def status():
    """
    define static route for /status endpoint
    returns string "OK".
    """
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    """
    define dynamic route for specifc username
    return full object for provided username, else 404 error
    """
    # return user info if user exists
    if username in users:
        return jsonify(users[username])
    # user not found - status 404 with error message
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    handles POST request to add a new user
    """
    # try convert JSON to python object
    try:
        data = request.get_json()
    # invalid JSON
    except BadRequest:
        return jsonify({"error": "Invalid JSON"}), 400

    # username missing
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # username already exists
    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # add user & return confirmation meesage
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


# run flask development server
if __name__ == "__main__":
    app.run()
