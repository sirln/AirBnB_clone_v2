#!/usr/bin/python3
'''
Module to start Flask web application
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def salutation():
    ''' Welcome Message '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    ''' Display “HBNB” '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def dynamic_routing_c(text):
    '''
    Display “C ” followed by the value of the text variable
    replacing underscore “_” symbols with a space “ ”
    '''
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dynamic_routing_python(text):
    '''
    Display “Python ” followed by the value of the text variable
    replacing underscore “_” symbols with a space “ ”
    '''
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def dynamic_routing_number(n):
    '''
    Display “n is a number” only if n is an integer
    '''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def dynamic_routing_number_template(n):
    '''
    Display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    '''
    number = n
    return render_template('5-number.html', number)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def dynamic_routing_number_odd_or_even(n):
    '''
    Display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    '''
    num = n
    if (n % 2) == 0:
        type = 'even'
    else:
        type = 'odd'
    return render_template('6-number_odd_or_even.html', num=num, type=type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
