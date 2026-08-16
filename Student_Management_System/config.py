import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


DATA_FILE = os.path.join(BASE_DIR,"database", "student_data.json")

SECRET_KEY = "student_management_system_secret_key"

DEBUG = True

STUDENTS_PER_PAGE  = 10