from soundscript import app
# from flask__sqlalchemy import SQLAlchemy
# from flask_login import  UserMixin
# from config import Config
# from dotenv import load_dotenv
# import os

# load_dotenv() #load env. variable from keys.env

# app = Flask(__name__, template_folder="../templates", 
                        # static_folder="../static")
# app.config.from_object('config.DevelopmentConfig')

# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

if __name__ == '__main__':
    app.run(debug=True)