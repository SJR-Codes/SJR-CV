"""
* SJR-CV 20.10.2022
* cv.py
* CV class
* Created by Samu Reinikainen
"""
import funcs as f
from settings import Sets

class CV:
    def __init__(self, template = "template.html", style="style.css"):
        self.settings = Sets()
        self.html = f.fetchFile("tmpl/" + template)
        #set inline styles to template        
        self.style = f.fetchFile("tmpl/" + style)
        self.html = self.html.replace("*STYLE*", self.style)
        
    def setBaseHtmlSettings(self, settings: dict) -> None:
        """
        Set htmlSettings values to html placeholders.
        :param html: html source as string
        :type html: str
        :param settings: settings as dict
        :type settings: dict
        :return: string
        :rtype: str
        """
        for key, val in settings.items():
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