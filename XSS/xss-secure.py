from flask import Flask, render_template, request, make_response
import db

###
# Information about the security settings, can be found here: https://flask.palletsprojects.com/en/2.0.x/security/
###

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    response = make_response(render_template('index.html',
                                             comments=comments,
                                             search_query=search_query))

    # Tell the browser where it can load various types of resource from.
    # This header should be used whenever possible, but requires some work to define the correct policy for your site.
    response.headers['Content-Security-Policy'] = "default-src 'self'"

    # The browser will try to prevent reflected XSS attacks by not loading the page if the request contains something
    # that looks like JavaScript and the response contains the same data.
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == "__main__":
    app.run(debug=True)
