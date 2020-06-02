# Diceware Passphrase Generator
Generates rolls and passphrase client side

## To Install:
1. Clone repository: 
    ```
    $ git clone https://github.com/GongJunior/dw-Web.git
    ```
1. Run the following to 
    ```
           $ python -m venv venv
           $ .\venv\Scripts\activate
    (venv) $ pip install -r requirements.txt
    ```
1. Required environment variables are:
    * FLASK_APP=start.py
    * FLASK_ENV=production
    Execute *env.ps1* to set defaults
    ```
    (venv) $ & .\env.ps1
    ```
1. In root directory, create *.env* file hold key environment variables
1. Setup your database and store URI in DB_URI
1. Run migrations then start flask
    ```
    (venv) $ flask db init
    (venv) $ flask db upgrade
    (venv) $ flask init-db
    (venv) $ flask run
    ```

