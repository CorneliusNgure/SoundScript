import os
from flask import Flask
from config.config import DevelopmentConfig


app = Flask(__name__, template_folder="../templates", 
                        static_folder="../static")
app.config.from_object(DevelopmentConfig)

env = os.environ.get("FLASK_ENV")
if env == "production":
    app.config.from_object("config.config.ProductionConfig")
elif env == "testing":
    app.config.from_object("config.config.TestingConfig")
else:
    app.config.from_object("config.config.DevelopmentConfig")

from soundscript import routes