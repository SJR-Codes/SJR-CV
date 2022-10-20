"""
* SJR-CV 19.10.2022
* application.py
* Flask application for CV web page
* Created by Samu Reinikainen
"""
from flask import Flask
import settings as sets
import funcs as f

class CV:
    def __init__(self, template = "template.html", style="style.css"):
        self.htmlTemplate = f.fetchFile(template)
        self.style = f.fetchFile(style)
        #set inline styles to template
        self.htmlTemplate = self.htmlTemplate.replace("*STYLE*", self.style)
        self.htmlTemplate = f.setHtmlSettings(self.htmlTemplate, sets.htmlSettings)
        
    def addBody(self, content:str) -> None:        
        """
        Insert content to html body.
        :param content: html content
        :type content: str
        :return: None
        """
        self.htmlTemplate = self.htmlTemplate.replace("*BODY*", content)

    #define what class instance prints when print() or str()
    def __str__(self):
         return self.htmlTemplate

#initialize flask app
app = Flask(__name__)

#initialize CV
#override defaults: cv = CV(template="*yourtemplate.html*", style="*yourstyle.css*")
cv = CV()
cv.addBody("<h1>CV 20.10.2022</h1>")

#respond all queries with CV page
@app.route("/")
def hello():
    return str(cv)


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    #run flask app
    app.run()