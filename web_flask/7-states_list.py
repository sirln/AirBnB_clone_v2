#!/usr/bin/python3
'''
Module to start Flask web application
'''
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    '''
    Display list of all State objects present in DBStorage
    sorted by name (A->Z)
    '''
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_session(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
