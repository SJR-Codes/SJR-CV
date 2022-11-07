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
        #fetch html template
        self.html = f.fetchFile("tmpl/" + self.settings._baseTemplate)
        #set inline styles to template
        self.style = f.fetchFile("tmpl/" + self.settings._styleCss)
        self.html = self.html.replace("*STYLE*", self.style)
        #set base html settings, title, author etc.
        for key, val in self.settings._htmlBase.items():
            self.html = self.html.replace(key, val)
        self.content = ""
    
    def addBlock(self, template, data):
        #html = f.fetchFile(template)
        self.content += f.setPlaceHolders(f.fetchFile(template), getattr(Sets, data))

    def addMultiBlock(self, outertmpl, innertmpl, data):
        tmp = ""

        innerhtml = f.fetchFile(innertmpl)
        for para in getattr(Sets, data).get("Content"):
            tmp += f.setPlaceHolders(innerhtml, para)
        
        block = f.fetchFile(outertmpl)
        block = block.replace("*TITLE*", getattr(Sets, data).get("*TITLE*"))
        block = block.replace("*CONTENT*", tmp)

        self.content += block

    def addBody(self) -> None:
        """
        Insert content to html body.
        :return: None
        """
        self.html = self.html.replace("*BODY*", self.content)

    #define what class instance prints when print() or str()
    def __str__(self):
         return self.html