class Config:
    SECRET_KEY = 'E3);d5I;>CO£NbD@3\3Fm'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'venta'
    SQLALCHEMY_DATABASE_URI = 'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}