# activate the virtual environment
#   $ python3 -m venv venv
#   $ source venv/bin/activate
# confirm that flask is installed
#   $ pip install flask

# flask 'looks' for an app called app.py to start
 

from flask import Flask
app = Flask(__name__)

# app = Flask(__name__) creates an instance of the Flask class

#   $ flask run

# this doesn't have any content, but will start a server AKA expect a 404 error

# flask run starts server in production mode

# to run in development mode, set the FLASK_ENV environment variable to development
#   $ FLASK_ENV=development flask run


# SO in summation 
#   $ python3 -m venv venv
#   $ source venv/bin/activate
#   $ pip install flask
#   $ flask run
#   $ FLASK_ENV=development flask run

# leave out FLASK_ENV=development to run in production mode

# to stop the server, press ctrl + c

# OR to make it easier to run debug per session, set the FLASK_ENV environment variable to development
#   $ export FLASK_ENV=development
#   $ flask run
# then, when flask run is run, it will run in debug mode automatically, during this session

# *********OR*********

# add the export command to the end of the .bash_profile file

