import csv
import os

import bcrypt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class UserAuth:
    def __init__(self, user_type:str, user_email:str, password:str):
        self.userType = user_type
        self.user_email = user_email
        self.password = password


class UserAuthManager:
    def __init__(self, user_login_details:UserAuth):
        self.user = user_login_details

    def check_password(self, entered_password: str, stored_hashed_password) -> bool:
        return bcrypt.checkpw(entered_password.encode(), stored_hashed_password.encode())

    def check_if_user_exists(self, row:dict, user):
        return user.user_email == row['email']

    def is_valid_user(self):
        with open(BASE_DIR + f'/database/{self.user.userType.lower()}.csv', 'r') as file:
            database = csv.DictReader(file)
            for row in database:
                if self.check_if_user_exists(row) and self.check_password(self.user.password, row['password']):
                    return True

        return False

    def authenticate_user(self):
        if self.is_valid_user():
            return f"welcome, {self.user.user_email}"






