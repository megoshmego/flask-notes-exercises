developement mode 
# $ Flask_ENV=development flask run


# difference between a library and a framework - library is a collection of code that you 
# can use in your application, framework is a collection of code that you can use to build your application

# Flask is a framework

# Flask is a microframework - it is a framework that is designed to be small and simple

# Flask is a web framework - it is a framework that is designed to build web applications

# import the Flask class from the flask library 
# from flask import Flask

# create an instance of the Flask class

# web applications in general provide -- 

#   handle web requests
#   produce dynamic HTML 
#   handle forms 
#   handle cookies  
#   connect to databases 
#   provide user log-in / log-out
#   cache pages for performance 

# *****Making Responses*****

# a function that returns web response is called a view
    a response is a string
    typically a string of HTML

# A function that returns an HTML string

    @app.route('/hello')
    def say_hello():
        """Return simple "Hello" Greeting"""
        return "HELLO THERE"

        # ^^^ this will actually return HELLO there onto the web page 




# DEBUG_INTRO.PY

    includes a simple flask example of: 

        use of route decorators
        creating a root page 
        linking to another page using <ahref>
        returning a string inside the python function
        returning html inside the python function 


# QUERY STRINGS 

    in the URL, we can also use key value pairs for returning the desired web page result

    commonly used for searching, or filtering through data
        ex. ->  reddit using 'sort by new'

        https://www.reddit.com/r/ProgrammerHumor/new/  

            will look for ProgrammerHumor subreddit
            will sort by new


    @app.route('/search')
def search():
    """Handle GET requests like /search?term=fun"""

    term = request.args.get["term"]
    return f'<h1>Search results for: {term}</h1>'



# returns localhost:5000/search?term=fun
                                 ^   ^
            query param and key  ^   ^
                                     ^
                               value ^ 

# the value of the query parameter is the part of the url that comes after the equals sign
# the query parameter is the key, and the value of the query parameter is the value

# the request.args.get() method is used to get the value of a query parameter
# the request.args.get() method takes the name of the query parameter as an argument
# the request.args.get() method returns the value of the query parameter, or None if the query parameter # is not present


@app.route('search')
def search():
    term = request.args.get("term")
    sort = request.args.get("sort")
    return f'<h1>Search results for: {term}</h1><p>Sort by: {sort}</p>'

# the above code will return the search term and the sort parameter, if it exists

# to search for a term and sort by a parameter, add it to the end of the url, like so:  
# http://
# localhost:5000/search?term=fun&sort=popular


    localhost:5000/search?term=fun&sort=popular
                                    ^       ^
                query param and key ^       ^
                                            ^
                                      value ^


 # ON QUERY PARAMETERS and URL PARAMETERS
 
    
    








