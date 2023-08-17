from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')  # Load configuration from config.py

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, title="ChatGPT Bot API", description="API for managing ChatGPT prompts")

from app import routes 