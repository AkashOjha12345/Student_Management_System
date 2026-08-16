import config

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from controllers.student_controller import StudentController
from models.student import Student
from utils.validator import Validator


app = Flask(__name__)
app.config.from_object(config)
app.secret_key = config.SECRET_KEY

controller = StudentController()


# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        total=controller.total_students(),
        average=controller.average_marks(),
        topper=controller.top_student()
    )


# -------------------------------
# View All Students
# -------------------------------
@app.route("/students")
def students():

    student_list = controller.get_all_students()

    return render_template(
        "students.html",
        students=student_list
    )


# -------------------------------
# Add Student
# -------------------------------
@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_id = request.form["student_id"]

        if controller.get_student_by_id(student_id):
            flash("Student ID already exists!", "danger")
            return redirect(url_for("add_student"))

        if not Validator.validate_email(request.form["email"]):
            flash("Invalid Email Address!", "warning")
            return redirect(url_for("add_student"))

        if not Validator.validate_phone(request.form["phone"]):
            flash("Invalid Phone Number!", "warning")
            return redirect(url_for("add_student"))

        student = Student(
            student_id=request.form["student_id"],
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            age=int(request.form["age"]),
            gender=request.form["gender"],
            course=request.form["course"],
            department=request.form["department"],
            email=request.form["email"],
            phone=request.form["phone"],
            address=request.form["address"],
            marks=float(request.form["marks"]),
            attendance=0
        )

        controller.add_student(student)

        flash("Student Added Successfully!", "success")

        return redirect(url_for("students"))

    return render_template("add_student.html")


# -------------------------------
# Student Details
# -------------------------------
@app.route("/student/<student_id>")
def student_details(student_id):

    student = controller.get_student_by_id(student_id)

    if student is None:
        return render_template("error.html")

    return render_template(
        "student_details.html",
        student=student
    )


# -------------------------------
# Edit Student
# -------------------------------
@app.route("/edit/<student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    student = controller.get_student_by_id(student_id)

    if student is None:
        return render_template("error.html")

    if request.method == "POST":

        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "marks": float(request.form["marks"])
        }

        controller.update_student(student_id, data)

        flash("Student Updated Successfully!", "success")

        return redirect(url_for("students"))

    return render_template(
        "edit_student.html",
        student=student
    )


# -------------------------------
# Delete Student
# -------------------------------
@app.route("/delete/<student_id>", methods=["GET", "POST"])
def delete_student(student_id):

    student = controller.get_student_by_id(student_id)

    if student is None:
        return render_template("error.html")

    if request.method == "POST":

        controller.delete_student(student_id)

        flash("Student Deleted Successfully!", "success")

        return redirect(url_for("students"))

    return render_template(
        "delete_student.html",
        student=student
    )


# -------------------------------
# Search Student
# -------------------------------
@app.route("/search")
def search_student():

    keyword = request.args.get("keyword", "")

    students = []

    if keyword:
        students = controller.search_student(keyword)

    return render_template(
        "search_student.html",
        students=students
    )


# -------------------------------
# Custom 404 Page
# -------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404


# -------------------------------
# Run Application
# -------------------------------
if __name__ == "__main__":
    app.run(debug=config.DEBUG)