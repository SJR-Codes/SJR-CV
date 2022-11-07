"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""
from flask import Flask
from settings import Sets
import funcs as f
from cv import CV

#initialize flask app
app = Flask(__name__)

#initialize CV
cv = CV()

cv.addBlock("tmpl/head.html", "_htmlHead")
cv.addBlock("tmpl/about.html", "_htmlAbout")
cv.addMultiBlock("tmpl/block.html", "tmpl/experience.html", "_htmlExperience")

cv.addBody()

#respond all queries with CV page
@app.route("/")
def hello():
    return str(cv)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    #run flask app
    app.run()