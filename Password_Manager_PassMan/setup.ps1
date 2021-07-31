if (!(Test-Path env)){
    python -m venv env
}
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\env\Scripts\Activate.ps1
pip install -r .\requirements.txt
$env:FLASK_APP = "app.app:app"
$env:FLASK_ENV = "development"
