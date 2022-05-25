#!/usr/bin/python3
""" web application that fetches data from the storage engine """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display an HTML page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session():
    """Method to handle tear_down_appcontext"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
