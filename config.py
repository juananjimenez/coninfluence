import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY ') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RECAPTCHA_SITE_KEY = os.getenv('RECAPTCHA_SITE_KEY')
    RECAPTCHA_SECRET_KEY= os.getenv('RECAPTCHA_RECAPTCHA_KEY')
    #FORM_SECRET_KEY = os.getenv('FORM_SECRET_KEY')
    FORM_SECRET_KEY = "Juanan"

class ProductionConfig(Config):
    DB_USER_PROD = os.getenv('DB_USER_PROD')
    DB_PASS_PROD = os.getenv('DB_PASS_PROD')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ DB_USER_PROD + ':' + DB_PASS_PROD + '@us-cdbr-east-06.cleardb.net/heroku_281d095a401b2e6'
    #FORM_SECRET_KEY = os.getenv('FORM_SECRET_KEY')
    FORM_SECRET_KEY = "Juanan"
    DEBUG = False
    

class DevelopmentConfig(Config):
    DB_USER_DEV = os.getenv('DB_USER_DEV')
    DB_PASS_DEV = os.getenv('DB_PASS_DEV')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER_DEV + ':' + DB_PASS_DEV + '@localhost/PrecioLuzDB'
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_USER_DEV = os.getenv('DB_USER_DEV')
    DB_PASS_DEV = os.getenv('DB_PASS_DEV')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER_DEV + ':' + DB_PASS_DEV + '@localhost/PrecioLuzDB'