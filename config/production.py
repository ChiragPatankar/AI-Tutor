import os

from config.development import Config as DevConfig


class ProductionConfig(DevConfig):
    DEBUG = False
    TESTING = False

    # Override with production settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Production specific settings
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True