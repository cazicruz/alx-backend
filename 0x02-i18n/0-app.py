#!/usr/bin/env python3
""" Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSECRETKEY"
babal = Babel(app)

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
