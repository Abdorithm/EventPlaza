#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import render_template, url_for, flash, redirect, request
from event_plaza import app, bcrypt, db
from event_plaza.forms import RegistrationForm, LoginForm, UpdateProfileForm
from event_plaza.models import User
from flask_login import login_user, current_user, logout_user, login_required


with app.app_context():
    """ The database will work in the app context """
    db.create_all()

@app.route('/', strict_slashes=False)
def landing():
    """ Renders the landing page """
    return render_template('landing.html')

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """ Renders the log in page """
    if current_user.is_authenticated:
        flash('Already logged in.', 'success')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        with app.app_context():
            user = User.query.filter_by(email=form.email.data).first()
            print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check email and password', 'error')
            return redirect(url_for('login'))
    return render_template('log_in.html', form=form)

@app.route('/signup', strict_slashes=False, methods=['GET', 'POST'])
def signup():
    """ Renders the signup page """
    if current_user.is_authenticated:
        flash('You are already registered.', 'success')
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        with app.app_context():
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                        email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
        flash('Account created for {} {}!'.format(form.first_name.data,
                                                 form.last_name.data),
                                                 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', form=form)

@app.route('/signout', strict_slashes=False)
def logout():
    """ logs the user outs"""
    logout_user()
    return redirect(url_for('landing'))

@app.route('/home', strict_slashes=False)
@login_required
def home():
    """ Renders the home page that contains the user's events"""
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('your_events.html', image_file=image_file)

@app.route('/about', strict_slashes=False)
def about():
    """ Renders the dashboard page """
    return render_template('about.html')

@app.route('/dashboard', strict_slashes=False)
@login_required
def dashboard():
    """ Renders the dashboard page """
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('dashboard.html', image_file=image_file)


@app.route('/dashboard/create_task', strict_slashes=False)
@login_required
def create_task():
    """ Renders the dashboard page """
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('create_task.html', image_file=image_file)

@app.route('/profile', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def profile():
    """ Renders the dashboard page """
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated!')
        return redirect(url_for('profile'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', image_file=image_file, form=form)
