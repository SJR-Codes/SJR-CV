"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""
from flask import Flask
from settings import SETS
import funcs as f
from cv import CV

#initialize flask app
app = Flask(__name__)

#initialize CV
#override defaults: cv = CV(template="*yourtemplate.html*", style="*yourstyle.css*")
cv = CV()
cv.setBaseHtmlSettings(SETS._htmlBase)

html = f.fetchFile("tmpl/head.html")
headHtml = f.setPlaceHolders(html, SETS._htmlHead)

html = f.fetchFile("tmpl/about.html")
aboutHtml = f.setPlaceHolders(html, SETS._htmlAbout)

html = f.fetchFile("tmpl/experience.html")
block = f.fetchFile("tmpl/block.html")
experienceHtml = f.loopSetPH(html, block, SETS._htmlExperience)

cv.addBody(headHtml+aboutHtml+experienceHtml)

#respond all queries with CV page
@app.route("/")
def hello():
    return str(cv)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    #run flask app
    app.run()