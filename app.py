# Import dependencies
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)

# Create flask routines
@app.route('/')

def hello_world():
    return 'Hello world'

# Run flask app