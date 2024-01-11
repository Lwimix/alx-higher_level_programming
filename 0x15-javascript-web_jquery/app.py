#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def print():
    return render_template('2-main.html')

if __name__ == '__main__':
    app.run()
