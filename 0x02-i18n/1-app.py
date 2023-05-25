#!/usr/bin/env python3
""" Flask app"""
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_babel import Babel


app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSECRETKEY"
basedir = os.path.abspath(os.path.dirname(__file__))
babal = Babel(app)

class Config(object):
    LANGUAGES = ["en", "fr"]
    babel.default_locale='en'
    babel.default_timezone='UTC'


@app.route('/')
def index():
    return render_template('1-index.html')
