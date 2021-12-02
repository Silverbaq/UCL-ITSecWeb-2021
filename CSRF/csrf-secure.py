from flask import Flask, render_template, request, make_response
from flask_wtf.csrf import CSRFProtect
import db

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="This is a secret!!!",
)
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    response = make_response(render_template('index_secure.html',
                                             comments=comments,
                                             search_query=search_query))
    return response


if __name__ == "__main__":
    app.run(debug=True)
