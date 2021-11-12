# Web authentication

## Setup
* Install dependencies. `pip install -r requirements.txt`

## Basic 
This is a simple application using `basic auth`.

* Run the application with the command `python basic_auth.py`.

Then navigate to `http://localhost:5000` and fill out the form.

## Digest
This is a simple application using `digest auth`.

* Run the application with the command `python digest_auth.py`.

Then navigate to `http://localhost:5000` and fill out the form. 

## Token
This is a simple Flask application using `token/bearer auth`.

* Run the application with the command `python token_auth.py`.

To communicate with the application, use something like `curl`.

* `curl -X GET -H "Authorization: Bearer <jws-token>" http://localhost:5000/`
* E.g. `curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNjczNDg0NiwiZXhwIjoxNjM2NzM4NDQ2fQ.eyJ1c2VybmFtZSI6ImpvaG4ifQ.Zn6i2DLxYr7ql3848RzPNtKvKk1WgiEVJxdk0mXs4kEsxm_4JX9xcCFnQ_0ru0g7tMDewtJwpY65YdPijKLAXQ" http://localhost:5000/`


## Session
This is a simple Flask application, which uses session for auth.

* Run the application which the command `python session_auth.py`

The following endpoints should be available:
* Dashboard: `http://127.0.0.1:5000/`
* Login: `http://127.0.0.1:5000/login`
* Logout `http://127.0.0.1:5000/logout`