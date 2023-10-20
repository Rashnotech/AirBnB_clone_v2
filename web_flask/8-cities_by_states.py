#!/usr/bin/python3
""" a module that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    data = storage.all(State)
    cities = data['cities']
    if storage_type != 'db':
        cities = State.cities
    return render_template('8-cities_by_states.html', data=data, cities=cities)


@app.teardown_appcontext
def teardown():
    storage.close()


if __name__ == '__main__':
    app.run(host=0.0.0.0)
