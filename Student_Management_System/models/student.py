from datetime import datetime

class Student:
    """
    Student Model Class
    """

    def __init__(
        self,
        student_id,
        first_name,
        last_name,
        age,
        gender,
        course,
        department,
        email,
        phone,
        address,
        marks=0,
        attendance=0
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.course = course
        self.department = department
        self.email = email
        self.phone = phone
        self.address = address
        self.marks = marks
        self.attendance = attendance
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        return "F"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "gender": self.gender,
            "course": self.course,
            "department": self.department,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "marks": self.marks,
            "attendance": self.attendance,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data.get("student_id", ""),
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            age=data.get("age", 0),
            gender=data.get("gender", ""),
            course=data.get("course", ""),
            department=data.get("department", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            address=data.get("address", ""),
            marks=data.get("marks", 0),
            attendance=data.get("attendance", 0),
        )

    def update(self, data):
        self.first_name = data.get("first_name", self.first_name)
        self.last_name = data.get("last_name", self.last_name)
        self.age = data.get("age", self.age)
        self.gender = data.get("gender", self.gender)
        self.course = data.get("course", self.course)
        self.department = data.get("department", self.department)
        self.email = data.get("email", self.email)
        self.phone = data.get("phone", self.phone)
        self.address = data.get("address", self.address)
        self.marks = data.get("marks", self.marks)
        self.attendance = data.get("attendance", self.attendance)

    def __str__(self):
        return (
            f"{self.student_id} | "
            f"{self.full_name} | "
            f"{self.course} | "
            f"{self.department}"
        )


           


