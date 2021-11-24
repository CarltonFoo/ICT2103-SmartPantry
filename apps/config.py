import os
from decouple import config

class Config(object):
    # Set up SQL username and password
    SQL_USERNAME=os.getenv("SQL_USERNAME")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")
    SQL_DATABASE=os.getenv("SQL_DATABASE")

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{SQL_USERNAME}:{SQL_PASSWORD}@localhost:3306/{SQL_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Debug': DebugConfig
}
