from flask import Flask, render_template
from flask__sqlalchemy import SQLAlchemy
from flask_login import  UserMixin

app = Flask(__name__, template_folder="../frontend/templates", 
                        static_folder="../frontend/static")
db = SQLAlchemy(app) #database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #connect app file to database file
app.config['SECRET_KEY'] = 'SoundScriptsecretkey'



@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)