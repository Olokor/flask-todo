from models import Student
class Create_student_view:
    def __init__(self):
        self.student_info = []

    def get_info(self):
        print("""
        fill the form in the following manner:
        'first_name', 'last_name', 'email', 'password'
        """)

        self.student_info = input().split(",")
        self.student_info[3] = int(self.student_info[3])
        return self.student_info
