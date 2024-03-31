#from flask import Flask
from database import db

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    note = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, nullable=False)


