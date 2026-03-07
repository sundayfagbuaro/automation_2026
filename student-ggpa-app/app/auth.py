# app/auth.py
from flask import Blueprint, request, jsonify, render_template_string
from app.models import Student, db

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")

# POST route (API)
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    student = Student(username=data["username"], email=data["email"])
    student.set_password(data["password"])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student registered"}), 201

# GET route (browser form)
@auth_bp.route("/register", methods=["GET"])
def register_form():
    return render_template_string("""
    <h1>Register Student</h1>
    <form method="POST" action="/auth/register">
      Username: <input name="username"><br>
      Email: <input name="email"><br>
      Password: <input name="password" type="password"><br>
      <button type="submit">Register</button>
    </form>
    """)

@auth_bp.route("/register", methods=["POST"])
def register_post():

    # If request comes from API (curl / fetch)
    if request.is_json:
        data = request.get_json()
    else:
        # If request comes from browser form
        data = request.form

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    student = Student(username=username, email=email)
    student.set_password(password)

    db.session.add(student)
    db.session.commit()

    if request.is_json:
        return jsonify({"message": "Student registered"}), 201
    else:
        return f"Student {username} registered successfully!"


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    student = Student.query.filter_by(username=data["username"]).first()
    if student and student.check_password(data["password"]):
        return jsonify({"message": "Login successful", "ggpa": student.ggpa})
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/login", methods=["GET"])
def login_form():
    return render_template_string("""
    <h1>Login</h1>
    <form method="POST" action="/auth/login">
      Username: <input name="username"><br>
      Password: <input name="password" type="password"><br>
      <button type="submit">Login</button>
    </form>
    """)