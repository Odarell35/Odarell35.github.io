from flask import Flask
from models.User_model import User
from models import storage
from views.app_views import app_views
from views.login import app_login
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'key_0624191673'

app.register_blueprint(app_views)
app.register_blueprint(app_login)

login_manager = LoginManager()
login_manager.login_view = 'app_login.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.errorhandler(404)
def page_not_found(err):
    """handler"""
    return {"error": "Not found"}, 404

@app.errorhandler(400)
def page_not_found(err):
    """handler"""
    msg = err.description
    return msg, 400


if __name__ == "__main__":
    app.run(debug=True)
