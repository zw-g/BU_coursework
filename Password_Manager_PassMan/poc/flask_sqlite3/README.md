# Flask and SQLite3 POC

## Getting started

1. In the `poc` directory, setup a virtual environment of your choice. You can
execute the following to start and activate a virtual environment:
```
pip install virtualenv
virtualenv flask_sqlite3
source flask_sqlite3/bin/activate
```

2. Install dependencies
```
pip install flask
```
NOTE: `sqlite3` is included in the standard Python library ( > 2.5 )

3. Configure environment variables. On Mac you create environment variables
with:
```
export FLASK_APP=flask_sqlite3
export FLASK_ENV=development
```

4. Initialize SQLite3 database
```
flask initialize-database
```

5. Finally, run the application and open your browser to localhost port 5000.
```
flask run
```
