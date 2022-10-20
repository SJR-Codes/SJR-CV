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