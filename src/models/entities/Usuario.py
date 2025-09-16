from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, username, password, nombre=''):
        self.id = id
        self.username = username
        self.password = password
        self.nombre = nombre

    @classmethod 
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def generate_hash(cls, password):
        return generate_password_hash(password)

