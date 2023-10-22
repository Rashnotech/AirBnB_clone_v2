#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
from models import storage
from models import State
from models import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    state = storage.all(State)
    amenity = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=state,
                           amenities=amenity)


@app.teardown_appcontext
def teardown(self):
    """ teardown instances """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
