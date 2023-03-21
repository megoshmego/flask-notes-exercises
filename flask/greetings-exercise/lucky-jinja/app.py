from flask import Flask, render_template, request, redirect
from random import randint
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']='secret'
debug = DebugToolbarExtension(app)



@app.route("/form")
def show_form():
    """returns a form to input a username, which is sent to "/greet"""""
    return render_template("form.html")

COMPLIMENTS = ["Funny", "Tenacious", "Smart", "Trustworthy"]


@app.route("/greet")
def get_greeting():
    """returns a greeting with the name"""
    username = request.args["username"] 
    nice_thing = choice(COMPLIMENTS)
    # While this is the example this will NOT work, and next subject will fix it 
    return render_template("greet.html", username=username, compliment = nice_thing)
