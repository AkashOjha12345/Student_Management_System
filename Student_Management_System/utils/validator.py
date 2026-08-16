import re

class Validator:

    @staticmethod
    def validate_name(name):
        return bool(re.fullmatch(r"[A-Za-z]{2,50}",name.strip()))
    
    @staticmethod
    def validate_age(age):
        try:
            age = int(age)
            return 16 <= age <= 100
        except ValueError:
            return False
        
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(pattern, email))

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\+?[0-9\s\-()]{7,20}$"
        return bool(re.fullmatch(pattern, phone.strip()))

    @staticmethod
    def validate_marks(marks):
        try:
            marks = float(marks) 
            return 0 <=marks <=100

        except ValueError:
            return False


    @staticmethod
    def validate_attendance(attendance):
        try:
            attendance = float(attendance)
            return 0 <=attendance<=100
        except ValueError:
            return False

    @ staticmethod
    def validate_student_id(student_id):
        pattern = r"^STU\d{3,6}$"
        return bool (re.fullmatch(pattern,student_id))
           