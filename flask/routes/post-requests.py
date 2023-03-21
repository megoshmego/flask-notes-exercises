from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <body>
            <h1>I am ROOT!</h1>'
            <a href='/hello'>Go to Hello Page</a>
        </body>
    </html>
    """
    return html

# Below is the route decorator for the '/posting' page. It will NOT return the string "I am a request . . "
# BECAUSE the method is set to POST. It will return the string "I am a request..."
# once the method is changed to GET.


@app.route("/posting", methods=["POST"])
def posting():
    return "I made a request. I named the route and function posting, but this is till a GET request."


@app.route("/posting", methods=["GET"])
def posting2():
    return "I am a request. I know I am GET."


#######CORRECT EXAMPLE OF PYTHON POST REQUESTS########

@app.route('/add-comment')
def add_comment():
    return """
        <h1> Add a comment, for me to quickly forget </h1>
        <form method="POST">
        <input type= 'text' placeholder="comment" name="comment">
        <input type= 'text' placeholder="username" name="username">
        <button>Submit</button>
    </form>
    """



@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form.get("comment")
    username = request.form.get("username")
    return f"""
    <h1>Comment is finally saved<h1>
    <ul>
        <li>Comment: {comment}</li>
        <li>Username: {username}</li>
    </ul>
    """
