from flask import Blueprint, render_template, request, flash, jsonify
import json
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


