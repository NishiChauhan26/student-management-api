from flask import Flask, request, jsonify
import json
import os
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config["SECRET_KEY"] = "your-secret-key"
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


students = load_students()
next_id = max([s["id"] for s in students], default=0) + 1


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            token = token.replace("Bearer ", "")
            jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return decorated


@app.route("/")
def home():
    return {"message": "Student API is running!"}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or data.get("username") != VALID_USERNAME or data.get("password") != VALID_PASSWORD:
        return jsonify({"error": "Invalid username or password"}), 401

    token = jwt.encode(
        {
            "username": data["username"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({"token": token})


# CREATE - Add a new student (protected)
@app.route("/students", methods=["POST"])
@token_required
def add_student():
    global next_id
    data = request.get_json()

    if not data or "name" not in data or "course" not in data:
        return jsonify({"error": "name and course are required"}), 400

    student = {
        "id": next_id,
        "name": data["name"],
        "age": data.get("age"),
        "course": data["course"],
        "marks": data.get("marks")
    }
    students.append(student)
    next_id += 1
    save_students(students)
    return jsonify(student), 201


# READ - Get all students (public)
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# READ - Get one student by id (public)
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for s in students:
        if s["id"] == student_id:
            return jsonify(s)
    return jsonify({"error": "Student not found"}), 404


# UPDATE - Modify an existing student (protected)
@app.route("/students/<int:student_id>", methods=["PUT"])
@token_required
def update_student(student_id):
    data = request.get_json()

    for s in students:
        if s["id"] == student_id:
            s["name"] = data.get("name", s["name"])
            s["age"] = data.get("age", s["age"])
            s["course"] = data.get("course", s["course"])
            s["marks"] = data.get("marks", s["marks"])
            save_students(students)
            return jsonify(s)

    return jsonify({"error": "Student not found"}), 404


# DELETE - Remove a student (protected)
@app.route("/students/<int:student_id>", methods=["DELETE"])
@token_required
def delete_student(student_id):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            return jsonify({"message": f"Student {student_id} deleted"})

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)