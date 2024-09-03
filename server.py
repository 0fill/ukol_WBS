from flask import Flask,render_tamplate

app = Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html')