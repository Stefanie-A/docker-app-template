from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
#from dotenv import load_dotenv

app = Flask(__name__)

#load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"


db = SQLAlchemy(app)










#'postgresql://username:password@localhost/database_name'