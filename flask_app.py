from flask import Flask, redirect, url_for, render_template, request, session
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'changethis'
app.permanent_session_lifetime = timedelta(days=30)

@app.route('/')
def hello_world():
    return 'Buajajaja'

@app.route('/app/')
def home():
    if "id" in session:
        return redirect(url_for("usuario"))
    else:
        return redirect(url_for("login"))

@app.route('/app/login/', methods=['POST','GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["nombres"]
        session['user'] = usr
        return redirect(url_for("usuario"))
    elif 'user' in session:
        return redirect(url_for('usuario'))
    else:
        return render_template('login.html')

@app.route('/app/signup/', methods=['POST','GET'])
def signup():
    if request.method == "POST":
        usr = request.form["nombres"]
        session['user'] = usr
        return redirect(url_for("usuario"))
    elif 'user' in session:
        return redirect(url_for('usuario'))
    else:
        return render_template('signup.html')

@app.route('/app/usuario/')
def usuario():
    if 'user' in session:
        usr = session['user']
        return render_template('usuario.html', usuario=usr)
    else:
        return redirect(url_for("login"))

@app.route('/app/logout/')
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == "__main__":
    @app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)


    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                file_path = os.path.join(app.root_path,
                                         endpoint, filename)
                values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)
    app.run(host='0.0.0.0',port=8000, debug=True)