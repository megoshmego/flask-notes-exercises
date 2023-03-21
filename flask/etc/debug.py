# in venv $ pip install flask-debugtoolbar
# add to pip freeze > requirements.txt

# must import
# from flask_debugtoolbar import DebugToolbarExtension




from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.config['SECRET_KEY']= 'mego'
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template('index.html')


# using this ebug toolbar, can use SQLA, HTTP headers, TEMPLATES, ROUTE LIST, LOG, and CODE EXECUTION



