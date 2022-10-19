"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""
from flask import Flask
import settings

class CV:
    def __init__(self, template = "template.html", style="style.css"):
        self.htmlTemplate = fetchFile(template)
        self.style = fetchFile(style)

def main():
    #initialize flask app
    app = Flask(__name__)

    #initialize CV
    #override defaults: cv = CV(template="*yourtemplate.html*", style="*yourstyle.css*")
    #cv = CV()

    cv = "<h1>One moment, please...</h1>"

    #respond all queries with CV page
    @app.route("/")
    def hello():
        return cv

def fetchFile(filen: str) -> str:
    try:
        with open(filen, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit("Error: script file not found")

# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()