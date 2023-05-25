#!/usr/bin/env python3
""" Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babal = Babel(app)

class Config(object):
    SECRET_KEY = "MYSECRETKEY"
    LANGUAGES = ["en", "fr"]
    babel.default_locale='en'
    babel.default_timezone='UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
        """returns the htlm file for the route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
