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

    #define templates
    _baseTemplate = "template.html"
    _styleCss = "style.css"

    _htmlBase = {
        "*LANG*": "en",
        "*TITLE*": "Curriculum Vitae | Samu Reinikainen",
        "*DESC*": "Tiny CV app made with Python and served with Flask",
        "*AUTH*": "samu.reinikainen@gmail.com"
    }

    _htmlHead = {
        "*TITLE*": "Samu Reinikainen",
        "*SUBTITLE*": "Python Developer (Student)",
        "*LOCATION*": "Helsinki, Finland",
        "*DATE*": "24.11.2022",
        "*PIC*": "img/naama.png"
    }

    _htmlAbout = {
        "*TITLE*": "About Me",
        "*CONTENT*": "+15 years experience in ICT & software development.<br/>Entrepreneur, freelancer, employee. ERP, invoicing, HR management, Web, Warehouse management.<br/>Enthusiastically learning Python and looking for job."
    }

    _htmlExperience = {
        "*TITLE*": "Experience",
        "Content": [
            {
                "*YEAR*": "2023-", 
                "*COMPANY*": "contact to get your company here", 
                "*JOBTITLE*": "Python Developer (apprentice)", 
                "*DESC*": "Only good companies accepted. No unethical evil doers. Well, except if the pay is really good..."
            },
            {
                "*YEAR*": "2021-2022", 
                "*COMPANY*": "Stadin Safka", 
                "*JOBTITLE*": "Waste food handler", 
                "*DESC*": "Saving the world and getting good physical exercise."
            },
            {
                "*YEAR*": "2016-2017", 
                "*COMPANY*": "Kymppi Service Oy", 
                "*JOBTITLE*": "Warehouse worker", 
                "*DESC*": "Forklift driver & Excel/VB wizard."
            },
            {
                "*YEAR*": "2013-2015", 
                "*COMPANY*": "Eezy Osk", 
                "*JOBTITLE*": "Freelancer", 
                "*DESC*": "Backend stuff, Drupal modules, Web coding."
            },
            {
                "*YEAR*": "2009-2013", 
                "*COMPANY*": "Ajassa Ky", 
                "*JOBTITLE*": "Entrepreneur", 
                "*DESC*": "PHP coding, server administration, build, sell & support workstations."
            },
            {
                "*YEAR*": "2008-2009", 
                "*COMPANY*": "Pro-Equal Oy", 
                "*JOBTITLE*": "Partner", 
                "*DESC*": "Server administration, build, sell & support workstations."
            },
            {
                "*YEAR*": "2006-2008", 
                "*COMPANY*": "Carrot Oy", 
                "*JOBTITLE*": "Developer", 
                "*DESC*": "HR software development. PHP, MySQL"
            },
            {
                "*YEAR*": "2004-2006", 
                "*COMPANY*": "Volatile Software", 
                "*JOBTITLE*": "Entrepreneur", 
                "*DESC*": "Software development. PHP, MySQL"
            },
            {
                "*YEAR*": "2000-2004", 
                "*COMPANY*": "Bitblit Oy", 
                "*JOBTITLE*": "Programmer", 
                "*DESC*": "Web software development. MS Access, Visual Basic, PHP, PostgreSQL"
            },
        ]
    }

    _htmlEducation = {
        "*TITLE*": "Education",
        "Content": [
            {
                "*YEAR*": "2023", 
                "*SCHOOL*": "Taitotalo", 
                "*COURSE*": "Python basics", 
                "*DESC*": "7 months scratching the surface of todays ICT required skills: Python, Linux, Cloud, Data Analytics...",
                "*LINK*": "https://github.com/SJR-Codes/SJR-CV",
                "*TITLE*": "Final Project on GitHub"
            },
            {
                "*YEAR*": "2022", 
                "*SCHOOL*": "Harvard", 
                "*COURSE*": "CS50 Introduction to Programming with Python", 
                "*DESC*": "2 weeks speed run to prepare for next course.",
                "*LINK*": "https://github.com/SJR-Codes/CS50_codes/tree/main/final",
                "*TITLE*": "Final Project on GitHub"
            },
            {
                "*YEAR*": "2018", 
                "*SCHOOL*": "Opiframe", 
                "*COURSE*": "Internet of Things Developer", 
                "*DESC*": "6 months of getting acquainted with all things internet.",
                "*LINK*": "",
                "*TITLE*": ""
            },
            {
                "*YEAR*": "2000", 
                "*SCHOOL*": "Juva Vocational School", 
                "*COURSE*": "Vocational Qualification in Information Technology", 
                "*DESC*": "3 years of learning IT: Windows NT, ISDN etc. ancient history.",
                "*LINK*": "",
                "*TITLE*": ""
            },
        ]
    }

    _htmlFoot = {
        "*EMAIL*": "samu.reinikainen@gmail.com",
    }