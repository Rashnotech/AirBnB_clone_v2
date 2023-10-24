#!/usr/bin/python3
""" a module that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    mod = 0
    data = storage.all(State)
    if len(data.values()) != 0:
        for state in data.values():
            if state.id == id:
                mod = 1
                return render_template('9-states.html', data=state, mode=mod)
            elif state.id != id and id is not None:
                mod = 0
            else:
                mod = 2
    return render_template('9-states.html', data=data, mode=mod)


@app.teardown_appcontext
def teardown(self):
    """Teardown conext"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
