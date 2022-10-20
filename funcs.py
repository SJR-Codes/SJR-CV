"""
* SJR-CV 20.10.2022
* funcs.py
* Misc functions
* Created by Samu Reinikainen
"""
import base64 as b64

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
        exit(f"Error: script {filen} not found")

def fetchPic(filen: str) -> str:
    """
    Open filepath and return contents as base64 encoded string.
    :param filen: path & filename to file
    :type filen: str
    :return: string
    :rtype: str
    """
    try:
        with open(filen, 'rb') as bf:
            bfdata = bf.read()
            return b64.b64encode(bfdata).decode('utf-8')
    except FileNotFoundError:
        exit(f"Error: script {filen} not found")

def setPlaceHolders(filen: str, settings: dict) -> str:
    """
    Replace html template placeholders with values from settings.
    :param filen: template with placeholders
    :type html: str
    :return: html
    :rtype: str
    """
    html = fetchFile(filen)

    for key, val in settings.items():
        if key != "*PIC*":
            html = html.replace(key, val)
        else:
            pic = fetchPic(val)
            html = html.replace(key, pic)

    return html