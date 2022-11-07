"""
* SJR-CV 20.10.2022
* cv.py
* CV class
* Created by Samu Reinikainen
"""
import funcs as f
from settings import Sets

class CV:
    def __init__(self):
        #bring settings to self
        self.settings = Sets()
        self.html = f.fetchFile("tmpl/" + self.settings._baseTemplate)
        #set inline styles to template
        self.style = f.fetchFile("tmpl/" + self.settings._styleCss)
        self.html = self.html.replace("*STYLE*", self.style)
        #set base html settings, title, author etc.
        for key, val in self.settings._htmlBase.items():
            self.html = self.html.replace(key, val)
        
    def addBody(self, content:str) -> None:
        """
        Insert content to html body.
        :param content: html content
        :type content: str
        :return: None
        """
        self.html = self.html.replace("*BODY*", content)

    #define what class instance prints when print() or str()
    def __str__(self):
         return self.html