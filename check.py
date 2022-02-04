from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from os import environ
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)

# secrets.token_hex())
app.secret_key = environ['CHECK_SECRET_KEY']
password_hash = environ['CHECK_PASSWORD_HASH']


@app.route('/')
def index():
    if 'username' in session:
        return f'''
            <p>Logged in as {session["username"]}</p>
            <a href={url_for('logout')}>logout</a>
        '''
    return f'''
        <p>You are not logged in</p>
        <a href={url_for('login')}>login</a>
    '''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if pbkdf2_sha256.verify(password, password_hash):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            message = 'Incorrect password'
            return redirect(url_for('login', message=message))
    form = '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''
    message = request.args.get('message')
    if message:
        form = f'''
            <p>{message}</p>
        ''' + form
    return form


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
