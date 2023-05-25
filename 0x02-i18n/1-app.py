#!/usr/bin/env python3
""" Flask app"""
import os
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
babal = Babel(app)


class Config(object):
    SECRET_KEY = "MYSECRETKEY"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE ='en'
    BABEL_DEFAULT_TIMEZONE ='UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """ returns the html template for the view function"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
