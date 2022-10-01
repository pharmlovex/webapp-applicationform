from flask import Flask, render_template, flash, redirect
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager 



# create the app
app = Flask(__name__)
# Create instance of login
login = LoginManager(app)
login.login_view = 'login'
# configure the sqlite database relative to the app instance folder  
app.config.from_object(Config)
# Create the  extention for the db  
db = SQLAlchemy(app)
# initialize the app with the extention 
#db.init_app(app)
migrate = Migrate(app, db)


from app import routes, models
from app.form import LoginForm, RegistrationForm
