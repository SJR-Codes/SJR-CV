"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>My CV</h1></body></html>\n"