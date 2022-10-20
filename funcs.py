"""
* SJR-CV 20.10.2022
* funcs.py
* Misc functions
* Created by Samu Reinikainen
"""

def fetchFile(filen: str) -> str:
    """
    Open filepath and return contents as string.
    :param filen: path & filename to file
    :type filen: str
    :return: string
    :rtype: str
    """
    try:
        with open(filen, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit("Error: script file not found")


def setHtmlSettings(html: str, settings: dict) -> str:
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
        html = html.replace(key, val)

    return html