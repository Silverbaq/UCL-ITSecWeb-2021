from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


def init_db():
    db.create_all()
    admin = User(username='admin', email='admin@example.com', password='admin')
    guest = User(username='guest', email='guest@example.com', password='secret')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        users = User.query.filter_by(username=username)
    else:
        users = []
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
