# the looping magic is at line 37

from flask import Flask, render_template, request, redirect
from random import choice, randint
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
    return render_template("greet.html", username=username, compliment = nice_thing)
    # nice_thing is renamed because it is a variable, not a string  

@app.route("/lucky")
def lucky_num():
    """returns a lucky number"""
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num=num, msg="You are so lucky!")


@app.route('/spell/<word>')
def spell_word(word):
    """shows the letters in a word"""
    caps_word = word.upper()
    return render_template("spell.html", word=caps_word)
    # create a list of letters in the word in uppercase using looping and list comprehension