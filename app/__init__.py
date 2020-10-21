from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)


login = LoginManager(app)
login.blueprint_login_views = {
    "admin" : "admin.admin_login",
}

login.login_message_category='info'


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app import routes, models

from admin import admin_app
from admin import routes, models as admin_models
app.register_blueprint( admin_app )


@login.user_loader
def load_user(user_id):
    id = int(user_id.split("|")[0])
    endpoint = user_id.split("|")[1]
    if endpoint == 'admin':
        return admin_models.Admin.query.get(id)


