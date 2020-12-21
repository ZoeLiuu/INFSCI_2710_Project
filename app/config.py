import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zoeliuu851996@localhost/SmartPharm'
    SQLALCHELMY_TRACK_MODIFICATIONS = False
