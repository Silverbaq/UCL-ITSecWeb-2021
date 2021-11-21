from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


class User(object):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        query = "SELECT * FROM user WHERE username = '{}'".format(username)
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        fetched_data = cur.execute(query)
        users = [User(x[0], x[1], x[2], x[3]) for x in fetched_data]
    else:
        users = []
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
