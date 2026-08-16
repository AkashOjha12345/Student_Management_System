import json
import os

from config import DATA_FILE
from models.student import Student


class StudentController:

    def __init__(self):
        self.students = self.load_students()

   
    # Load Students
    
    def load_students(self):
        if not os.path.exists(DATA_FILE):
            return []

        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            return [Student.from_dict(student) for student in data]

        except Exception:
            return []

    
    # Save Students
    
    def save_students(self):
        with open(DATA_FILE, "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

   
    # Add Student
   
    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    
    # Get All Students
    
    def get_all_students(self):
        return self.students

    #
    # Get Student By ID
    
    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    
    # Update Student
    
    def update_student(self, student_id, data):
        student = self.get_student_by_id(student_id)

        if student:
            student.update(data)
            self.save_students()
            return True

        return False

    
    # Delete Student
    
    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)

        if student:
            self.students.remove(student)
            self.save_students()
            return True

        return False

    
    # Search Student
    
    def search_student(self, keyword):
        keyword = keyword.lower()

        result = []

        for student in self.students:
            if (
                keyword in student.student_id.lower()
                or keyword in student.full_name.lower()
                or keyword in student.course.lower()
                or keyword in student.department.lower()
            ):
                result.append(student)

        return result

    
    # Total Students
    
    def total_students(self):
        return len(self.students)

   
    # Sort By Name
    
    def sort_by_name(self):
        return sorted(
            self.students,
            key=lambda student: student.full_name.lower()
        )

    
    # Sort By Marks
    
    def sort_by_marks(self):
        return sorted(
            self.students,
            key=lambda student: student.marks,
            reverse=True
        )

    
    # Average Marks
    
    def average_marks(self):
        if not self.students:
            return 0

        total = sum(student.marks for student in self.students)
        return round(total / len(self.students), 2)

    
    # Top Performer
    
    def top_student(self):
        if not self.students:
            return None

        return max(
            self.students,
            key=lambda student: student.marks
        )