$env:FLASK_APP = "start.py"
$env:FLASK_ENV = "development"
#$env:FLASK_ENV = "production"
gci env: | where name -Like flask*