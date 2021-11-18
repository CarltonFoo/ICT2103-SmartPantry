# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/smartpantry'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Debug': DebugConfig
}
