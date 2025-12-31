
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import bcrypt, jwt, datetime, os
from functools import wraps

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET'] = os.getenv("JWT_SECRET", "dev_secret_key")

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority"
)

client = MongoClient(MONGO_URI)
db = client["user_mgmt"]
users = db["users"]

def token_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify({"error": "Token missing"}), 401
            try:
                data = jwt.decode(token, app.config['JWT_SECRET'], algorithms=["HS256"])
                current_user = users.find_one({"email": data["email"]})
                if role and current_user["role"] != role:
                    return jsonify({"error": "Access denied"}), 403
            except:
                return jsonify({"error": "Invalid token"}), 401
            return f(current_user, *args, **kwargs)
        return wrapper
    return decorator

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    if users.find_one({"email": data["email"]}):
        return jsonify({"error": "User exists"}), 409

    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": hashed,
        "role": "user",
        "status": "active",
        "created_at": datetime.datetime.utcnow()
    })
    return jsonify({"message": "Signup successful"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = users.find_one({"email": data["email"]})
    if not user or not bcrypt.checkpw(data["password"].encode(), user["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        "email": user["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['JWT_SECRET'], algorithm="HS256")

    return jsonify({"token": token, "role": user["role"]})

@app.route("/me", methods=["GET"])
@token_required()
def me(current_user):
    return jsonify({
        "name": current_user["name"],
        "email": current_user["email"],
        "role": current_user["role"]
    })

@app.route("/admin/users", methods=["GET"])
@token_required(role="admin")
def all_users(current_user):
    page = int(request.args.get("page", 1))
    limit = 10
    skip = (page - 1) * limit
    data = list(users.find({}, {"password": 0}).skip(skip).limit(limit))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
