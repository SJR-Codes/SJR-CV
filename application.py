"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""
from flask import Flask
import settings as sets
import funcs as f
import cv


#initialize flask app
app = Flask(__name__)

#initialize CV
#override defaults: cv = CV(template="*yourtemplate.html*", style="*yourstyle.css*")
mycv = cv.CV()
mycv.setHtmlSettings(sets.htmlSettings)
mycv.addBody("<h1>CV 20.10.2022</h1>")

#respond all queries with CV page
@app.route("/")
def hello():
    return str(mycv)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    #run flask app
    app.run()