#!/usr/bin/python3
'''
Module to start Flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def salutation():
    ''' Welcome Message '''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
