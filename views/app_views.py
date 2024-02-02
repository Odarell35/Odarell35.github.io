from flask import Blueprint, render_template, request, flash, jsonify
import json
from models import storage
from models.Books_model import Books
from models.Category_model import Category
from models.Review_model import Reviews
from models.User_model import User
from models.parent_model import Parentmodel
from flask_login import login_required, current_user

app_views = Blueprint('app_views', __name__)

@app_views.route('/Home', strict_slashes=False)
def home():
    """home page"""
    return "eBookClub"

@app_views.route('/About', strict_slashes=False)
def about():
    """About page"""
    return "About eBookClub"

@app_views.route('/Books', strict_slashes=False)
def books():
    """displays all books in the db"""
    books = []
    for book in storage.data(Books).values():
        books.append(book.to_dict())
    return jsonify(books)

