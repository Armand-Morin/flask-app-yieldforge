# -*- encoding: utf-8 -*-

import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')
