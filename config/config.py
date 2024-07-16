# import os

# class Config(object):
#     DEBUG = False
#     TESTING = False

#     SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

#     DB_NAME = 'production-db'
#     DB_USERNAME = 'root'
#     DB_PASSWORD = 'example'

#     UPLOADS = os.environ.get('UPLOADS') or os.path.join(os.getcwd(), 'uploads')

#     SESSION_COOKIE_SECURE = True

# class ProductionConfig(Config):
#     pass

# class DevelopmentConfig(Config):
#     DEBUG = True

#     DB_NAME = 'development-db'
#     DB_USERNAME = 'root'
#     DB_PASSWORD = 'example'

#     SESSION_COOKIE_SECURE = False

# class TestingConfig(Config):
#     TESIING = True

#     DB_NAME = 'development-db'
#     DB_USERNAME = 'root'
#     DB_PASSWORD = 'example'

#     SESSION_COOKIE_SECURE = False