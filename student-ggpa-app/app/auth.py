from flask import Blueprint, request, jsonify
from app.models import db, Student
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    student = Student(username=data["username"], email=data["email"])
    student.set_password(data["password"])
    db.session.add(student)
    db.session.commit()
    return jsonify(message="Registered successfully"), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    student = Student.query.filter_by(email=data["email"]).first()
    if student and student.check_password(data["password"]):
        token = create_access_token(identity=student.id)
        return jsonify(token=token)
    return jsonify(message="Invalid credentials"), 401