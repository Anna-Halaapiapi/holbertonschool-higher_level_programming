#!/usr/bin/python3
"""
provides basic auth and security in flask
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

# create flask app and set the secret key ("aS8d9f7gH3kL!2mN4pQzX1vR")
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "aS8d9f7gH3kL!2mN4pQzX1vR"

# Initialise JWT manager
jwt = JWTManager(app)

# Create a dict of users and their hashed passwords
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# create auth object to handle basic auth for routes
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]  # return the user object/dict
    return None


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# routes
@app.route("/login", methods=["POST"])
def login():
    """
    define route for login endpoint
    """
    # try convert JSON to python
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    # invalid JSON error handling
    except BadRequest:
        return jsonify({"error": "Invalid JSON"}), 400

    # check if user exists
    if username in users:
        stored_hash = users[username]["password"]
        # verify p/w
        if check_password_hash(stored_hash, password):
            # create JWT token
            token = create_access_token(identity={
                "username": username,
                "role": users[username]["role"]
            })
            # return token in JSON
            return jsonify({"access_token": token})
    # invalid username or p/w
    return jsonify({"error": "Unauthorised"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    define route for basic protected endpoint
    """
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    define route for /jwt-protected
    protected route with JWT token
    """
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    define route for admin_only endpoint
    only accessible for users with admin role
    """
    # get username from JWT token
    identity = get_jwt_identity()
    role = identity.get("role")

    # check user exists
    if role == "admin":
        return jsonify({"message": "Admin Access: Granted"})

    # return error if user doesnt exist
    return jsonify({"error": "Admin access required"}), 403


# run flask development server
if __name__ == "__main__":
    app.run()
