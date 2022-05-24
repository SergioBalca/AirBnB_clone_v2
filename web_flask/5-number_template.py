#!/usr/bin/python3
"""  starts a Flask web application:
        - /: display Hello HBNB
        - /hbnb: display HBNB
        - /c/<text>: display "C" followed by the value of text
        - /python/<text>: display "Python" followed by
                          the value of text
            - the default value of text is "is cool"
        - /number/<n>: display "n is a number" only if n is an int
        - /number_template/<int:n>: display a HTML template only if n is int
"""


from flask import Flask
from flask import render_template
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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def variable_python(text='is cool'):
    """Returns 'Python' is the value of text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns 'n is a number' if n is an int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """Returns an HTML template if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
