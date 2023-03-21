from flask import Flask

app = Flask(__name__)

# routes generally refer to mapping of different pages of a website
# the route decorator is used to tell Flask what URL should trigger our function

# below is the route decorator for the root, or homepage. It is the default page that is loaded when you 
# go to the website. It returns html "I am ROOT!" and a link to the hello page, with the ahref tag
# if we didn't include a root decorator, the default page would be a 404 error, but /hello would still work

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


# Below is the route decorator for the hello page. It returns the string 'Hello, World!' without 
# any html tags


@app.route('/hello')
def hello_world():
    return 'Hello, World!'



# the route decorator below for page '/hello-in-html' returns HTML for displaying the 
# string 'HELLO I AM HTML!' in the browser as an h1 header 

@app.route('/hello-in-html')
def hello_world():
    html = """
    <html>
        <body>
            <h1>HELLO I AM HTML!</h1>'
        </body>
    </html>
    """
    return html









