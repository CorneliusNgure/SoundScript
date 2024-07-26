import os

"""
Configuration settings for the application.

This module contains different configuration classes for various environments:
- `Config`: Base configuration class with common settings.
- `ProductionConfig`: Configuration for the production environment.
- `DevelopmentConfig`: Configuration for the development environment.
- `TestingConfig`: Configuration for the testing environment.
"""

class Config(object):
    """
    Base configuration class.

    This class provides the default configuration settings for the application. 
    It includes settings for debug mode, testing mode, and database credentials.
    """

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

   # UPLOADS = os.environ.get('UPLOADS') or os.path.join(os.getcwd(), 'soundscript', 'uploads')

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    """
    Production configuration class.

    Inherits from `Config` and applies settings specific to the production environment.
    """
    pass

class DevelopmentConfig(Config):
    """
    Development configuration class.

    Inherits from `Config` and applies settings specific to the development environment.
    """

    DEBUG = True
    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    """
    Testing configuration class.

    Inherits from `Config` and applies settings specific to the testing environment.
    """
    
    TESTING = True
    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    SESSION_COOKIE_SECURE = False