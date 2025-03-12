from Migration import Migration
from models.lecturer import Lecturer


class Course:
    table_headers = ['course_id', 'course_name', 'lecturer']
    def __init__(self, course_id, course_name, lecturer:Lecturer|None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_lecturer = lecturer


    def save(self):
        migration = Migration()
        record = {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_lecturer': self.course_lecturer
        }
        migration.add_record(f"{migration.BASE_DIR}/database/course.csv", Course, record)


    def assign_lecturer(self, lecturer:Lecturer):
        self.lecturer = lecturer

    def __str__(self):
        return
