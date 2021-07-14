from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, RadioField, PasswordField
from wtforms.fields.html5 import IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import hashlib
import binascii

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def __repr__(self):
        return ('User: {},{}'.format(self.name))

    def get_hashed_password(password):
        """Hash a password for storing."""
        # the value generated using os.urandom(60)
        os_urandom_static = b"ID_\x12p:\x8d\xe7&\xcb\xf0=H1\xc1\x16\xac\xe5BX\xd7\xd6j\xe3i\x11\xbe\xaa\x05\xccc\xc2\xe8K\xcf\xf1\xac\x9bFy(\xfbn.`\xe9\xcd\xdd'\xdf`~vm\xae\xf2\x93WD\x04"
        salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(stored_password_hash, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password_hash[:64]
        stored_password = stored_password_hash[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


class LoginForm(FlaskForm):
    name = StringField('User name')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')


@app.route('/init')
def init():
    db.create_all()

    admin = User.query.filter(User.name=='admin').first()
    if admin == None:
        admin = User(id=1, name='admin', password=User.get_hashed_password('Passw0rd'),
                     first_name='King', last_name='Kong')
        db.session.add(admin)
        db.session.commit()

    return '<h1>Initial configuration done</h1>'

@app.route('/')
def index():
    return '<h1>H3ll0</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    return '<h1>You are logged out</h1>'


@app.route('/docs')
def docs():

    return 'You have access to protected docs'


@app.route('/secrets')
def secrets():

    return 'You have access to protected secrets'


if __name__ == '__main__':
    app.run()