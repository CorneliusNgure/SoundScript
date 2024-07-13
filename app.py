from flask import Flask, render_template
# from flask__sqlalchemy import SQLAlchemy
from flask_login import  UserMixin
from config import Config
from dotenv import load_dotenv
import os

load_dotenv() #load env. variable from keys.env

app = Flask(__name__, template_folder="../frontend/templates", 
                        static_folder="../frontend/static")
app.config.from_object('config.DevelopmentConfig')

# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

@app.route('/')
def index_page():
    print(app.config['DB_NAME'])
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

if __name__ == '__main__':
    app.run(debug=True)