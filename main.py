from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
origins = [
    'http://localhost:8000',
    'http://localhost:3000'
]
CORS(app, origins=origins, supports_credentials=True)

# In-memory database
items_db = []

@app.route("/form/", methods=["GET"])
def check():
    name = request.args.get("name", "")
    email = request.args.get("email", "")
    
    if name_empty(name):
        return 'Please enter a valid name'
    
    elif email_empty(email):
        return 'Please enter a valid email'
    
    elif email_exists(email):
        return 'Email already exists'
    
    else:
        items_db.append({"name": name, "email": email})
        return 'Thanks'

@app.route("/items/", methods=["GET"])
def get_items():
    return jsonify(items_db)

# Helper functions
def name_empty(name):
    return name == '' or name is None

def email_empty(email):
    return email == '' or email is None

def email_exists(email):
    for item in items_db:
        if email == item["email"]:
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True, port=8000)
