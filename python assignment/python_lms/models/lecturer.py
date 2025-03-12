import bcrypt

from Migration import Migration

bcrypt.gensalt()
class Lecturer:
    table_header = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, first_name:str, last_name:str, email:str, password:str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.hash_password(password)

    def save(self):
        migration = Migration()
        record = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

        migration.add_record(f"{migration.BASE_DIR}/database/lecturer.csv", Lecturer, record)


    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()  # Generate a random salt
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed

    def __str__(self):
        return "{" +f"""
        first_name: {self.first_name},
        last_name: {self.last_name},
        email: {self.email},
        
""" +"}"