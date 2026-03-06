from flask import Flask, jsonify
from app.config import Config
from app.models import db
from flask_jwt_extended import JWTManager
from app.auth import auth_bp
from app.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    @app.route("/dashboard/<int:student_id>")
    def dashboard(student_id):
        student = db.session.get(Student, student_id)
        if student:
            return jsonify(username=student.username, ggpa=student.ggpa)
        return jsonify(message="Student not found"), 404

    return app