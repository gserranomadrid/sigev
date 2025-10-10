from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, username, password, nombre=''):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__nombre = nombre

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_nombre(self):
        return self.__nombre

    @classmethod 
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def generate_hash(cls, password):
        return generate_password_hash(password)

