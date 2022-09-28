from flask import Flask, render_template, flash, redirect
from config import Config
from form import LoginForm


app=Flask(__name__)
app.config.from_object(Config)

# Create a route decorator
@app.route("/")
def index():
    user = [
            {"Username":"Alfred"},
            {"School":"Teesside University"}
    ]
    articles = [
        {
          "Author" : {"Username":"Ifedayo"},
          "journal": "Nature",
            "Year" : 2018 
        },
        {
          "Author" : {"Username":"Jane"},
          "journal": "Lancet",
            "Year" : 2022 
        },
        {
          "Author" : {"Username":"Bimbo"},
          "journal": "Pubmed",
            "Year" : 2020
        }
    ]
    return render_template("index.html", title = None, user=user, articles=articles)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login request from user ={}, remember_me={}".format(
            form.username.data, form.remember_me.data))     
        return redirect("/")           
    return render_template("login.html", title="Sign in", form=form)
