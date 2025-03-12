class Create_lecturer_view:
    def __init__(self):
        self.lecturer_info = []

    def get_lecturer_info(self):
        print("""
                fill the form in the following manner:
                'first_name', 'last_name', 'email', 'age', 'gender', 'class', password
                """)

        self.lecturer_info = input().split(",")
        return self.lecturer_info

