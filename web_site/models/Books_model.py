#!/usr/bin/pyhton3
"""Books Model"""
from web_site import db
from web_site import models

class Books(db.Model):
    """collection of Books"""
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(128))
    Author = db.Column(db.String(128))
    Catergory_name = db.Column(db.String(128), nullable=False)
    Book_description = db.Column(db.String(1024), nullable=False)
    ref_link = db.Column(db.String(128), nullable=True)
