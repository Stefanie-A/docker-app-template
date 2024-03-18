#from flask import Flask
from database import db

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Task = db.Column(db.String(80), unique=True, nullable=False)
    Note = db.Column(db.String(120), unique=True, nullable=False)
    Date = db.Column(db.Date, nullable=False)

