#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to serve JSON data
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Endpoint to check status
@app.route('/status')
def status():
    return "OK"

# Endpoint to get user details by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

# Endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return "Username is required", 400
    if username in users:
        return "User already exists", 409
    
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]})

# Run the Flask development server
if __name__ == "__main__":
    app.run()
