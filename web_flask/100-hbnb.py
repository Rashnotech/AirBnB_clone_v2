#!/usr/bin/python3
""" Airbnb web application """

from flask import Flask, render_template
from models import storage
from models import State
from models import Amenity
from models import Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ airbnb clone """
    state = storage.all(State)
    amenity = storage.all(Amenity)
    place = storage.all(Place)
    return render_template('100-hbnb.html', states=state,
                           amenities=amenity, places=place)


@app.teardown_appcontext
def teardown(self):
    """ airbnb teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
