from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Buajajaja'

@app.route('/app/')
def home():
    return render_template('index.html')
@app.route('/resources/<path>')
def get_assets(path):
	return render_template(f'assets/{path}')