$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
gci env: | where name -Like flask*