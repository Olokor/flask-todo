import bcrypt

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

# Example usage
hashed_password = hash_password("securepassword")
# print(hashed_password)
