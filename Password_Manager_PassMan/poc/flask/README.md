# Flask POC
This tiny sample shows flask in action, with page templates and .css styling.

## TOC
* [Prerequisites](#prerequisites)
* Setup and Run
  * [Windows and VS Code](#windows-and-vs-code)
  * [Mac](#mac)

## Prerequisites
* Python 3.9

## Setup and Run

### Windows and VS Code
* Open this folder using VS Code.
* Open a terminal window in VS Code (Terminal -> New Terminal).
* Create a virtual environment: `python -m venv env`
* Before we can activate the virtual environment, we need to set the execution policy for the user:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
* Activate the virtual environment: `.\env\Scripts\Activate.ps1`
* Install flask: `pip install flask`
* Export environment variables required by flask:
```
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
```
* Run the flask app: `flask run`
* You should see output similar to:
```
 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 640-300-998
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
* Open a web browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* You should be able to see the Log In page.

### Mac
_\<TODO>_
