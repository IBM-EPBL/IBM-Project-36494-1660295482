from flask import Flask, render_template, request, redirect, url_for, session, flash
from markupsafe import escape
from flask import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')