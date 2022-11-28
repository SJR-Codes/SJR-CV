"""
* SJR-CV 19.10.2022
* settings.py
* misc settings for CV
* Created by Samu Reinikainen
"""
from dataclasses import dataclass #Python 3.7->

#freeze class to make it immutable
@dataclass(frozen=True)
class Sets_fi:

    #define templates
    _baseTemplate = "template.html"
    _styleCss = "style.css"
    _lang = "fi"

    _htmlBase = {
        "*LANG*": "fi",
        "*TITLE*": "Curriculum Vitae | Samu Reinikainen",
        "*DESC*": "Pieni CV-sovellus, kirjoitettu Pythonilla ja tarjoillaan Flaskillä",
        "*AUTH*": "samu.reinikainen@gmail.com"
    }

    _htmlHead = {
        "*TITLE*": "Samu Reinikainen",
        "*SUBTITLE*": "Python kehittäjä (opiskelija)",
        "*LOCATION*": "Helsinki, Suomi",
        "*DATE*": "24.11.2022",
        "*PIC*": "img/naama.png"
    }

    _htmlAbout = {
        "*TITLE*": "Lyhyesti",
        "*CONTENT*": "+15 vuotta kokemusta ICT & sovelluskehityksestä.<br/>Yrittäjä, freelancer, työläinen. ERP, laskutus, henkilöstöhallinta, Web, varastohallinta.<br/>Innokkaasti opettelen Pythonia ja etsiskelen töitä."
    }

    _htmlExperience = {
        "*TITLE*": "Kokemus",
        "Content": [
            {
                "*YEAR*": "2023-", 
                "*COMPANY*": "firmanne nimi tähän, ole yhteydessä", 
                "*JOBTITLE*": "Python kehittäjä (harjoittelija)", 
                "*DESC*": "Vain kivoja firmoja. Ei pahiksille. Paitsi jos palkka on iso..."
            },
            {
                "*YEAR*": "2021-2022", 
                "*COMPANY*": "Stadin Safka", 
                "*JOBTITLE*": "Hävikkiruoan käsittelijä", 
                "*DESC*": "Maailman pelastamista ja hyvää treeniä."
            },
            {
                "*YEAR*": "2016-2017", 
                "*COMPANY*": "Kymppi Service Oy", 
                "*JOBTITLE*": "Varastotyöntekijä", 
                "*DESC*": "Koodaava trukkikuski."
            },
            {
                "*YEAR*": "2013-2015", 
                "*COMPANY*": "Eezy Osk", 
                "*JOBTITLE*": "Freelancer", 
                "*DESC*": "Backend hommia, Drupal moduuleita, Web-koodausta."
            },
            {
                "*YEAR*": "2009-2013", 
                "*COMPANY*": "Ajassa Ky", 
                "*JOBTITLE*": "Yrittäjä", 
                "*DESC*": "PHP ohjelmointia, palvelinten ylläpitoa, työasemien kasausta, myyntiä ja tukea."
            },
            {
                "*YEAR*": "2008-2009", 
                "*COMPANY*": "Pro-Equal Oy", 
                "*JOBTITLE*": "Partner", 
                "*DESC*": "Palvelinten ylläpitoa, työasemien kasausta, myyntiä ja tukea."
            },
            {
                "*YEAR*": "2006-2008", 
                "*COMPANY*": "Personel Henkilöstöpalvelut Oy", 
                "*JOBTITLE*": "Ohjelmoija", 
                "*DESC*": "Henkilöstöhallinnon työkalujen kehitystä. PHP, MySQL"
            },
            {
                "*YEAR*": "2004-2006", 
                "*COMPANY*": "Volatile Software", 
                "*JOBTITLE*": "Yrittäjä", 
                "*DESC*": "Ohjelmointia. PHP, MySQL"
            },
            {
                "*YEAR*": "2000-2004", 
                "*COMPANY*": "Bitblit Oy", 
                "*JOBTITLE*": "Ohjelmoija", 
                "*DESC*": "Web-ohjelmointia. MS Access, Visual Basic, PHP, PostgreSQL"
            },
        ]
    }

    _htmlEducation = {
        "*TITLE*": "Koulutus",
        "Content": [
            {
                "*YEAR*": "2023", 
                "*SCHOOL*": "Taitotalo", 
                "*COURSE*": "Ohjelmoinnin perusteet, Python", 
                "*DESC*": "7kk pintaraapaisua nykypäivän ICT-taitoihin: Python, Linux, Cloud, Data Analytics...",
                "*LINK*": "https://github.com/SJR-Codes/SJR-CV",
                "*TITLE*": "Projekti GitHub:ssa"
            },
            {
                "*YEAR*": "2022", 
                "*SCHOOL*": "Harvard", 
                "*COURSE*": "CS50 Introduction to Programming with Python", 
                "*DESC*": "2 viikon pikainen tutustuminen Pythoniin.",
                "*LINK*": "https://github.com/SJR-Codes/CS50_codes/tree/main/final",
                "*TITLE*": "Projekti GitHub:ssa"
            },
            {
                "*YEAR*": "2018", 
                "*SCHOOL*": "Opiframe", 
                "*COURSE*": "Internet of Things kehittäjä", 
                "*DESC*": "6kk tutustumista internetin juttuihin.",
                "*LINK*": "",
                "*TITLE*": ""
            },
            {
                "*YEAR*": "2000", 
                "*SCHOOL*": "Juvan Ammattioppilaitos", 
                "*COURSE*": "Tietotekniikan perustutkinto", 
                "*DESC*": "3 vuotta IT:n opettelua: Windows NT, ISDN jne. muinaista historiaa.",
                "*LINK*": "",
                "*TITLE*": ""
            },
        ]
    }

    _htmlFoot = {
        "*EMAIL*": "samu.reinikainen@gmail.com",
    }