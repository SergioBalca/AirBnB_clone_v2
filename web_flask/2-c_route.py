#!/usr/bin/python3
""" starts a Flask web application that:
    - /: display Hello HBNB!
    - /hbnb: display HBNB
    - /c/<text>: display "C" followed by the
                 value of the text variable
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable_c(text):
    """Returns 'C' and the value of text"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
