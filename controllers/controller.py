from flask import render_template, request
from app import app

@app.route('/')
def home():
    return "This is the home directory"