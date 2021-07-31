# PassMan application
This is the main PassMan application.

## Prerequisites
* [Python 3.9](https://www.python.org/downloads/)

## Setup
* Open the folder `BUMETCS673OLSum21P2` using VS Code.
* Open a terminal window in VS Code (Terminal -> New Terminal).
* Run the setup script:
  * On Windows: `.\setup.ps1`
  * On Mac/Linux: `. ./setup.sh`
    * If you get a _Permission denied_ error, you can make the script executable using: `chmod u+x ./setup.sh`

## Run PassMan
* Follow the instructions in [Setup](#setup)
* Initialize the database: `flask init-db`
* Seed the database: `flask seed-db`
* Run the flask app: `flask run`
* Open a web browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* You should see the Log In page.

## Run all tests
* Follow the instructions in [Setup](#setup)
* Run all tests using: `python -m unittest discover -v`

## Code coverage report
* Follow the instructions in [Setup](#setup)
* Run test suite and gather data: `coverage run --branch -m unittest discover`
* Report the results: `coverage report`
* You should see the code coverage results.
