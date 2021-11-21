from flask import (Flask, render_template, request, redirect, session)

app = Flask(__name__)
app.secret_key = "THIS-IS-A-SECRET"

user = {"username": "admin", "password": "password"}


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/')

        return "<h1>Wrong username or password</h1>"

    return render_template("login.html")


@app.route('/')
def dashboard():
    if 'user' in session and session['user'] == user['username']:
        return '<h1>Welcome to the dashboard</h1>'

    return '<h1>You are not logged in.</h1>'


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
