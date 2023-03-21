from flask import Flask, render_template, request, redirect, random
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']='secret'
debug = DebugToolbarExtension(app)



@app.route("/lucky")
def show_lucky_num():
    """example of a simple dynamic template"""

    num = randint(1, 100)
    return render_template("lucky.html", lucky_num=num, msg="You are so lucky!")