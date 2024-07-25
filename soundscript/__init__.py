import os
from flask import Flask
from config.config import DevelopmentConfig


app = Flask(__name__, template_folder="../templates", 
                        static_folder="../static")

app.config.from_object(DevelopmentConfig)

# app.config['UPLOADS'] = os.environ.get('UPLOADS') or os.path.join(os.getcwd(), 'uploads')

app.config['UPLOADS'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(app.config['UPLOADS']):
    os.makedirs(app.config['UPLOADS'])

env = os.environ.get("FLASK_ENV")
if env == "production":
    app.config.from_object("config.config.ProductionConfig")
elif env == "testing":
    app.config.from_object("config.config.TestingConfig")
else:
    app.config.from_object("config.config.DevelopmentConfig")

from soundscript import routes