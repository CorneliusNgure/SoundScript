from soundscript import app

"""
This script initializes and runs the Flask application.

It sets up the application by importing the `app` object 
from the `soundscript` module.

The module runs the Flask application in debug mode when 
the script is executed directly.

"""

# from flask__sqlalchemy import SQLAlchemy
# from flask_login import  UserMixin
# from config import Config
# from dotenv import load_dotenv
# import os

# load_dotenv() #load env. variable from keys.env

# app.config.from_object('config.DevelopmentConfig')

# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

if __name__ == '__main__':
    app.run(debug=True)