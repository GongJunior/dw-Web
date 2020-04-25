$env:FLASK_APP = "dw"
$env:FLASK_ENV = "development"
gci env: | where name -Like flask*