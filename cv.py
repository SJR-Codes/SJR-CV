"""
* SJR-CV 20.10.2022
* cv.py
* CV class
* Created by Samu Reinikainen
"""
import funcs as f
from settings import Sets
from settings_fi import Sets_fi


def renderCV(lang):
    #initialize CV
    cv = CV(lang)
    
    #add html blocks
    cv.addBlock("tmpl/head.html", "_htmlHead")
    cv.addBlock("tmpl/about.html", "_htmlAbout")
    cv.addMultiBlock("tmpl/block.html", "tmpl/experience.html", "_htmlExperience")
    cv.addMultiBlock("tmpl/block.html", "tmpl/education.html", "_htmlEducation")
    cv.addBlock("tmpl/foot.html", "_htmlFoot")

    #putting it all together
    cv.addBody()

    return cv

class CV:
    def __init__(self, lang):
        #bring settings to self
        if lang == "en":
            self.settings = Sets()
        elif lang == "fi":
            self.settings = Sets_fi()
        
        #fetch html template
        self.html = f.fetchFile("tmpl/" + self.settings._baseTemplate)
        #set inline styles to template
        self.style = f.fetchFile("tmpl/" + self.settings._styleCss)
        self.html = self.html.replace("*STYLE*", self.style)
        #set base html settings, title, author etc.
        for key, val in self.settings._htmlBase.items():
            self.html = self.html.replace(key, val)
        self.content = ""
   
    def addBlock(self, template:str, data:str) -> None:
        """
        Populate self.content with html block.
        :template:str = filename of template
        :data:str = variable name in settings class
        :return: None
        """
        self.content += f.setPlaceHolders(f.fetchFile(template), getattr(self.settings, data))
        
    def addMultiBlock(self, outertmpl:str, innertmpl:str, data:str) -> None:
        """
        Populate self.content with html block.
        :(inner/outer)template:str = filename of template
        :data:str = variable name in settings class
        :return: None
        """
        tmp = ""

        innerhtml = f.fetchFile(innertmpl)
        for para in getattr(self.settings, data).get("Content"):
            tmp += f.setPlaceHolders(innerhtml, para)
        
        block = f.fetchFile(outertmpl)
        block = block.replace("*TITLE*", getattr(self.settings, data).get("*TITLE*"))
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