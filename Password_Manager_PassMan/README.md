[![PassMan Automated Tests](https://github.com/BUMETCS673/BUMETCS673OLSum21P2/actions/workflows/python-app.yml/badge.svg)](https://github.com/BUMETCS673/BUMETCS673OLSum21P2/actions/workflows/python-app.yml)

# PassMan
Course: BU MET CS 673 Online Summer 2021  
Team #: 2

## Team members
|Member|Role|
|---|---|
|Francis Xavier Joseph Pulikotil|Team Lead, Requirements Lead|
|Alexander Dewhirst|Design and Implementation Lead|
|Zhaowei Gu|QA Lead|
|Andrew Klimentyev|Configuration Lead|
|Kayla Bayusik|Security Lead|

[See here for detailed member introductions](team.md).

## Project Description
Our project, **PassMan**, is a web application that allows users to store their passwords.

A lot of people use the same passwords on multiple websites. This is a problem because of the many leaks that occur each year. If hackers are able to recover a password for one website, they can simply try it with other websites and thus gain access to multiple accounts of the user.

To reduce such damage, it is advisable to use unique passwords on every website. These unique passwords should also be sufficiently strong to maximize security. A stronger password will be longer, and contain a mix of letters, digits, and special characters to make it more unpredictable.

Even the average person will have tens of accounts with different websites, and it becomes humanly difficult to keep track of so many strong passwords. This is where a password manager is useful - you keep all your strong passwords secure in the password manager application, and the password manager itself is secured with a single strong “master” password. Our project **PassMan** is a password manager application whose goal is to store passwords securely, while being easy to use.

## Code Style
* Classes and methods should be thoroughly commented with their desired functionality and purpose.
* Coding guidelines - please follow the one established by Pylint and PEP8: https://www.python.org/dev/peps/pep-0008/
* JavaScript - please follow the Airbnb’s style guide on GitHub: https://github.com/airbnb/javascript
* CSS - please follow the Airbnb’s style guide on GitHub: https://github.com/airbnb/css#rule-declaration

## Features
These are the essential features **PassMan** will support:
* [X] Register for PassMan, to gain access to the application.
* [X] Login to PassMan, to start using the applcation.
* [X] Logout from PassMan, so that privacy is maintained when not using the application.
* [X] Keep passwords encrypted, so that users are confident of the security of their passwords.
* [X] Access PassMan as a web application, with a clean and simple interface.
* [X] Generate strong, unique passwords, which are difficult to brute force.

These are the nice-to-have features **PassMan** _might_ support:
* [ ] Export passwords, to be backed up.
* [ ] Import passwords, from an exported backup.
* [ ] Copy passwords to the clipboard, to quickly be able to paste them elsewhere.
* [ ] Create a business account, so that all employees can manage their passwords with PassMan.

## Technology and Frameworks
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com)
* HTML5/JavaScript
* [pycrypto](https://pypi.org/project/pycrypto/)
* [Passlib](https://passlib.readthedocs.io)

## Setup and running
[See here for instructions on how to set up and run the PassMan application](app/README.md)
