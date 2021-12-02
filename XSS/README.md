# XSS

## Setup
* Install dependencies. `pip install -r requirements.txt`

## NB!
Jinja (Which is the name of the templating framework that is used together with Flask) has a XSS security feature build-in. This can be enabled/disabled by changing the value of the `{% autoescape true %}` to `true or false`, in the `index.html` file.   

## Run
* The `vulnerable` version can be run, by using the command: `python vulnerable.py` 

* For the `xss-secure` version, it can be run with the command: `python xss-secure.py`