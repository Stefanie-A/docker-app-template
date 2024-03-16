#from flask import Flask
from database import db

class Task(db):
    id = db.Column(db.Integer, primary_key=True)
    Task= db.Column(db.String(80), unique=True, nullable=False)
    Note= db.Column(db.String(120), unique=True, nullable=False)
    Date=db.column(db.Date, unique=True, nullable=False)
