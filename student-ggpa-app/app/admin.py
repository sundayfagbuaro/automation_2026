from flask import Blueprint, render_template, request
from app.models import db, Student

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin", methods=["GET", "POST"])
def admin_dashboard():
    if request.method == "POST":
        student_id = request.form["student_id"]
        new_ggpa = float(request.form["ggpa"])
        student = Student.query.get(student_id)
        if student:
            student.ggpa = new_ggpa
            db.session.commit()
    students = Student.query.all()
    return render_template("admin.html", students=students)