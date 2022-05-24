#!/usr/bin/python3
""" starts a Flask web application:
        - /: display Hello HBNB
        - /hbnb: display HBNB
        - /c/<text>: display "C" followed by the value of text
        - /python/<text>: display "Python" followed by
                          the value of text
            - the default value of text is "is cool"
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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def variable_python(text='is cool'):
    """Returns 'Python' is the value of text"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
