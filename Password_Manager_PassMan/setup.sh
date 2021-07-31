rm -rf env
python -m venv env
. env/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.app:app
export FLASK_ENV=development
