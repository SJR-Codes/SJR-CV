"""
* SJR-CV 19.10.2022
* settings.py
* misc settings for CV
* Created by Samu Reinikainen
"""
from dataclasses import dataclass #Python 3.7->

#freeze class to make it immutable
@dataclass(frozen=True)
class Sets:

    _baseTemplate = "template.html"
    _styleCss = "style.css"

    _htmlBase = {
        "*LANG*": "en",
        "*TITLE*": "Samu Reinikainen CV",
        "*DESC*": "Tiny CV app made with Python and served with Flask",
        "*AUTH*": "samu.reinikainen@gmail.com"
    }

    _htmlHead = {
        "*TITLE*": "Samu Reinikainen CV",
        "*SUBTITLE*": "Python Developer (Student)",
        "*LOCATION*": "Helsinki, Finland",
        "*DATE*": "20.10.2022",
        "*PIC*": "img/naama.png"
    }

    _htmlAbout = {
        "*TITLE*": "About Me",
        "*CONTENT*": "+15 years experience in ICT & software development.<br/>Entrepreneur, freelancer, employee. ERP, invoicing, HR management, Web, Warehouse management.<br/>Enthusiastically learning Python and looking for job."
    }

    _htmlExperience = {
        "*TITLE*": "Experience",
        "Content": [
            {"*YEAR*": "2022", "*COMPANY*": "not yet", "*JOBTITLE*": "Developer", "*DESC*": "Lorem ipsum sic dolores amet..."},
            {"*YEAR*": "2021", "*COMPANY*": "Stadin Safka", "*JOBTITLE*": "Waste food handler", "*DESC*": "Lorem ipsum sic dolores amet..."},
        ]
    }

    _htmlEducation = {
        "*TITLE*": "Education",
        "Content": [
            {"*YEAR*": "2022", "*SCHOOL*": "Taitotalo", "*COURSE*": "Python basics", "*DESC*": "Lorem ipsum sic dolores amet..."},
            {"*YEAR*": "2022", "*SCHOOL*": "Harvard", "*COURSE*": "CS50 Python", "*DESC*": "Lorem ipsum sic dolores amet..."},
        ]
    }