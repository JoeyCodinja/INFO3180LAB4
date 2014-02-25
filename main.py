"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import render_template

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def home():
  """Returns the hello World"""
  return ("Add '/catwalk' or '/madlib' in the url above to continue");

@app.route('/catwalk')
def catwalk():
    """Returns the home page for the CatWalk App"""
    return render_template('catwalk.html')
  
@app.route('/madlibs')
def madlibs():
  """ Returns the madlibs page"""
  return render_template('madlibs.html')
  
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404
