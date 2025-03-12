from Migration import Migration
import bcrypt
class Student:
    table_header = ['id', 'first_name', 'last_name', 'email', 'age', 'gender', 'class', 'password']

    def __init__(self, first_name: str, last_name: str, email: str, age: int, gender: str, student_class: str, password:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_class = student_class
        self.email = email
        self.gender = gender
        self.password = self.hash_password(password)

    def save(self):
        record = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'age': self.age,
            'gender': self.gender,
            'class': self.student_class,
            'password':self.password
        }
        migration = Migration()
        migration.add_record(f'{migration.BASE_DIR}/database/studentdb.csv', Student, record)

    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()  # Generate a random salt
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed

    def __str__(self):
        return "{"+ f"""
    first_name: {self.first_name},
    last_name: {self.last_name},
    email: {self.email},
    age: {self.age},
    student_class: {self.student_class},
    gender: {self.gender},
    """+"}"

