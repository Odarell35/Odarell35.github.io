from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask import flash
from models.User_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from models import storage
from flask_login import login_user, login_required, logout_user, current_user

app_login = Blueprint('app_login', __name__)


@app_login.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login_method():
    """method to log in"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user is not None:
            if check_password_hash(user.password, password):
                flash('LOGGED IN!')
                login_user(user, remember=True)
                return redirect(url_for('app_views.Home'))
            else:
                flash('Incorrect')
        else:
            flash('Incorrect')
        return render_template("login.html", user=current_user)

@app_login.route('/logout', strict_slashes=False)
def logout_method():
    """logs user out"""
    logout_user()
    return redirect(url_for('app_login.login'))

@app_login.route('/sign-up', strict_slashes=False, methods=['GET', 'POST'])
def sign_up_method():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        password = request.form.get('password')

        user_accounts = storage.data(User).values()
        for acc in user_accounts:
            if acc.email == email:
                flash('Email already exists.')
                #lif len(password1) < 7:
                #lash('Password must be at least 7 characters')
            else:
                dict_user = f`{ name="name1", surname="surname1", email="email1", password="{generate_password_hash(password1, method='sha256')}"
                new_user = User(**dict_user)
                storage.new(new_user)
                storage.save()
                login_user(new_user, remember=True)
                flash('Account created!')
                return "Accont created"

    return render_template("Register.html")

