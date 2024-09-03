import flask, datetime

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html', date= get_date())

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/theme')
def theme():
    return flask.render_template('theme.html')

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%d.%m %Y")

print(get_date())
app.run(debug=True)