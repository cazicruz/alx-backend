#!/usr/bin/env python3
""" Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSECRETKEY"
babal = Babel(app)

@app.route('/')
def index():
    return render_template('index.html')
