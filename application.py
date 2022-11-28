"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""
from flask import Flask
import cv

#initialize flask app
app = Flask(__name__)

#respond all queries with english CV page
@app.route("/")
def index():
    cvHtml = cv.renderCV("en")
    return str(cvHtml)
#respond with finnish CV page
@app.route("/fi")
def index_fi():
    cvHtml = cv.renderCV("fi")
    return str(cvHtml)

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    #run flask app
    app.run()