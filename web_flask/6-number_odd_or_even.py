#!/usr/bin/python3
"""tarts a Flask web"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hel_hbnb():
    """HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text: str):
    """display “C ” followed by the value"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text='is cool'):
    """display “Python ” followed by the value of the text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numb_template(n):
    """n inside the tag BODY"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """n is even|odd inside the tag BODY"""
    type = ('even' if n % 2 == 0 else 'odd')
    return render_template('6-number_odd_or_even.html', num=n, type=type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)