# currently, all routes are hard coded till now
# in the reddit example, Reddit developers would have to hard code the routes for each subreddit 
# BUT they can use variables 


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <body>
            <h1>Path Variables and Making Requests</h1>
            <p>Enter a subreddit name in the URL</p>
            <p>Example: /r/python</p>
        </body>
    </html>
    """
    return html


### begin example of code, above is for running if you want to test it out ###

@app.route('/r/<subreddit>')
def subreddit(subreddit):
    """Handle GET requests like /r/programmerhumor"""
    return f'<h1>Browsing the {subreddit} subreddit</h1>'

##### OR FROM THE SPRINGBOARD EXAMPLE #####

USERS = {
    "Whiskey": "Whiskey is a good dog",
    "Spike": "Spike is a good hedgehog",
}

@app.route('/users/<username>')
def show_user_profile(username):
### you HAVE to put the username in the function, otherwise it will not work, because the username is a variable in the route ###
    """Show the user profile for that user."""

    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"


##### ANOTHER EXAMPLE W/ POSTS CHOICES WITH INT#####

POSTS = {
    1: "This is a post",
    2: "This is another post",
    3: "This is yet another post",
    4: "This is the last post",
}


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show the post with the given id, the id is an integer."""
    post = POSTS[post_id]
    return f"""<p>{post}</p>"""

# if you do not specifiy that the post_id is an int, it will not work, because it will be a string, and the POSTS dict is an int



@app.route('r/<subreddit>/comments/<int:post_id>')
def comments(subreddit, post_id):
    """Show the comments for a post."""
    return f"<h1>Viewing comments for post with id {post_id} in the {subreddit} subreddit</h1>"


@app.route("/shop/<toy>")
def show_toy(toy):
    """Show toy details."""
    return f"<h1>Here is your {toy}</h1>"

# This is an example of a route that might be used for a business that sells toys.
# hardcoding into the route is not great, for example you might not always want to include the toy color

# The URL parameter feels like the subject of the page, query strings feel like action or details.





