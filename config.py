import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = True

# Enable debug mode.
DEBUG = True

# Connect to the database

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PASS + '@ldpg-cg840u1mbg53mc3r0d60-a:5432/coninfluence_postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#Test database
TEST_USER = os.getenv('TEST_USER')
TEST_PASS = os.getenv('TEST_PASS')

SQLALCHEMY_DATABASE_URI_TEST = 'postgresql://' + TEST_USER + ':' + TEST_PASS + '@localhost:5432/coninfluence_test'
SQLALCHEMY_TRACK_MODIFICATIONS = False