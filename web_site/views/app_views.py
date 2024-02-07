from flask import Blueprint, render_template, request, flash, jsonify
import json
from web_site import db, app
from web_site.models.Books_model import Books
from web_site.models.Category_model import Category
from web_site.models.Review_model import Reviews
from web_site.models.User_model import User
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


@app_views.route('/Category', strict_slashes=False)
def category():
    categories = Category.query.all()
    
    return render_template("categories.html", categories=categories, title='categories')

@app_views.route('/books', strict_slashes=False)
def books():
    books = Books.query.all()

    return render_template("books.html", books=books, title='books')

@app_views.route('/book_by_category', strict_slashes=False)
def list_books():
    categories = Category.query.all()
    books_by_category = {}

    for category in categories:
        books = Books.query.filter_by(Catergory_name=category.category_name).all()
        books_by_category[category.category_name] = books

    return render_template('books_by_cat.html', books_by_category=books_by_category)

@app_views.route('/single_book/<int:book_id>', strict_slashes=False)
def single_book(book_id):
    book = Books.query.get(book_id)

    if book:
        return render_template('single_book.html', book=book)
    else:
        return ('NOT FOUND'), 404
