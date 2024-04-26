#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, url_for, flash, redirect
from models.engine.db_storage import DBStorage
from .forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd685ddbe85e8fa0e7fb24d5aeb994e8f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb:///plaza.db'
bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
db = DBStorage(app)

@app.route('/', strict_slashes=False)
def landing():
    """ Renders the landing page """
    return render_template('landing.html')

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """ Renders the log in page """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com' and form.password.data == 'passwd':
            flash('You are logged in!', 'success')
            return redirect(url_for('events'))
        else:
            flash('Login unsuccessful, please check email and password', 'error')
    return render_template('log_in.html', form=form)

@app.route('/signup', strict_slashes=False, methods=['GET', 'POST'])
def signup():
    """ Renders the signup page """
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {} {}!'.format(form.first_name.data,
                                                 form.last_name.data),
                                                 'success')
        return redirect(url_for('landing'))
    return render_template('sign_up.html', form=form)

@app.route('/events', strict_slashes=False)
def events():
    """ Renders the events' page """
    return render_template('your_events.html')

@app.route('/about', strict_slashes=False)
def about():
    """ Renders the dashboard page """
    return render_template('about.html')

@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """ Renders the dashboard page """
    return render_template('dashboard.html')

@app.route('/team', strict_slashes=False)
def team():
    """ Renders the dashboard page """
    return render_template('team.html')

@app.route('/profile', strict_slashes=False)
def profile():
    """ Renders the dashboard page """
    return render_template('profile.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
