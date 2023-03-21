# the looping magic is at line 37

from flask import Flask, render_template, request, redirect
from random import choice, randint, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']='secret'
debug = DebugToolbarExtension(app)

@app.route("/")
def show_homepage():
    """shows the homepage"""
    html = """
    <html>
        <body>
            <h1>Homepage</h1>
         <p>Welcome to this simple app!</p>
         <a href="/form">Go to the form page if you like</a>
        </body>
    </html>
    """
    return html



@app.route("/form")
def show_form():
    """returns a form to input a username, which is sent to "/greet"""""
    return render_template("form.html")


@app.route("/form-2")
def show_form_2():
    return render_template("form-2.html")



COMPLIMENTS = ["Funny", "Tenacious", "Smart", "Trustworthy"]


@app.route("/greet")
def get_greeting():
    """returns a greeting with the name"""
    username = request.args["username"] 
    nice_thing = choice(COMPLIMENTS)    
    return render_template("greet.html", username=username, compliment = nice_thing)
    # nice_thing is renamed because it is a variable, not a string  

@app.route("/greet-2")
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    # using just 'request.args' will return an error if the user doesn't check the box because
    # there was no value for 'wants_compliments' in the query string
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet-2.html", username=username, wants_compliments=wants, compliments=nice_things)

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
