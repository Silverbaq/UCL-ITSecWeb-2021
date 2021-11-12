from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin"),
    "joe": generate_password_hash("doe")
}


@auth.verify_password
def verify(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route("/")
@auth.login_required
def hello():
    return 'hello, {}!'.format(auth.current_user())


if __name__ == '__main__':
    print(users)
    app.run()
