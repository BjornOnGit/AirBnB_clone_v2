#!/usr/bin/python3
"""
You must use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
To load all cities of a State:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_in_states():
    """renders a template that displayes the cities in a state"""
    states = storage.all("State").values()
    return (render_template('8-cities_by_states.html', states=states))


@app.teardown_appcontext
def teardown_db(exception):
    """close db connections on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
