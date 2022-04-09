from flask import Flask, render_template,flash, redirect, url_for, session
from nltk import flatten
import requests
import json

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('main.html')
if __name__ == '__main__':
    app.run(debug=True)
