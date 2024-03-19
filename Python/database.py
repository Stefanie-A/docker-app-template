from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
print(DB_PORT)

CON = app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
print(CON)

db = SQLAlchemy(app)

#'postgresql://username:password@localhost/database_name'