#!/usr/bin/python3
""" a module that start a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n): 
        return render_template('6-number_odd_or_even.html', value=n)


if __name__ == '__main__':
    app.run(host=0.0.0.0)
