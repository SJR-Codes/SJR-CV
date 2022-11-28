# SJR-CV
#### Demo: https://sjr-cv.azurewebsites.net/
#### Description:

SJR-CV was developed as final project for Taitotalo's Python course.
SJR-CV's purpose is to create CV as HTML and serve it with Flask.

## Getting Started

Modify provided settings.py to your own texts and run application.py. 

### Files
* **application.py**:
    * main code file
* **settings.py**:
    * settings and contents for CV
    * interpreter creates CV based on this file
* **cv.py**:
    * CV class
* **funcs.py**:
    * misc functions
* **tmpl/*.html**:
    * HTML-templates
* **tmpl/style.css**:
    * CV stylings
* **img/naama.png**:
    * authors face, preferably replace with your own
* **README.md**:
    * this file

### Dependencies

* Final Project Representer depends following external libraries:
    * Flask    ```(pip install flask)```
* and following internal libraries:
    * base64

### Executing program

* Run application.py, see Help for command line options
    ```
    python application.py
    ```
* Open in browser: http://127.0.0.1:5000

## Help

* Run with -h to see command line arguments.
    ```
    python application.py -h
    ```

## Author

Samu Reinikainen
samu.reinikainen@gmail.com

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the APACHE LICENSE, VERSION 2.0 License