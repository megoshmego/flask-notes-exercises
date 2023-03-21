
# Creating a Flask app that makes requests

# import the requests library

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <body>
            <h1>Query Parmeters and Making Requests</h1>
            <p>Enter a search term in the URL</p>
            <p>Example: /search?term=fun</p>
        </body>
    </html>
    """
    return html


@app.route('/search')
def search():
    """Handle GET requests like /search?term=fun"""

    term = request.args.get["term"]
    return f'<h1>Search results for: {term}</h1>'

# to search for a term, add it to the end of the url, like so:
# localhost:5000/search?term=fun

# the term is the query parameter, and the value is the value of the query parameter
# the query parameter is the part of the url that comes after the question mark
# the value of the query parameter is the part of the url that comes after the equals sign
# the query parameter is the key, and the value of the query parameter is the value

# the request.args.get() method is used to get the value of a query parameter
# the request.args.get() method takes the name of the query parameter as an argument
# the request.args.get() method returns the value of the query parameter, or None if the query parameter is not present

# the request.args.get() method is a dictionary-like object, so it has a get() method

@app.route('search')
def search():
    term = request.args.get("term")
    sort = request.args.get("sort")
    return f'<h1>Search results for: {term}</h1><p>Sort by: {sort}</p>'

# the above code will return the search term and the sort parameter, if it exists

# localhost:5000/search?term=fun&sort=popular
