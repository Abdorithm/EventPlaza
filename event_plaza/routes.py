#!/usr/bin/python3
""" Starts a Flask Web Application """
import secrets, os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from event_plaza import app, bcrypt, db
from event_plaza.forms import RegistrationForm, LoginForm, UpdateProfileForm, CreateEventForm, CreateTaskForm, RequestResetForm, ResetPasswordForm
from event_plaza.models import User, Event, Task
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
    events = Event.query.filter(Event.organizer.any(id=current_user.id)).all()

    return render_template('your_events.html', image_file=image_file, events=events, current_user=current_user)

@app.route('/about', strict_slashes=False)
def about():
    """ Renders the dashboard page """
    return render_template('about.html')

@app.route('/<event_name>/dashboard', strict_slashes=False)
@login_required
def dashboard(event_name: str):
    """ Renders the dashboard page """
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    event = Event.query.filter_by(name=event_name).first()

    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('home'))
    if current_user not in event.organizer:
        flash('You are not authorized to view this page', 'error')
        return redirect(url_for('home'))
    tasks = Task.query.filter_by(event_id=event.id).all()
    return render_template('dashboard.html', image_file=image_file, event=event, tasks=tasks)

@app.route('/<event_name>/dashboard/create_task', strict_slashes=False , methods=['GET', 'POST'])
@login_required
def create_task(event_name):
    """ Renders the dashboard page """
    form = CreateTaskForm()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    event = Event.query.filter_by(name=event_name).first()
    if not event:
        flash('Event not found', 'error')
        return redirect(url_for('home'))
    if current_user not in event.organizer:
        flash('You are not authorized to view this page', 'error')
        return redirect(url_for('home'))
    if form.validate_on_submit():
        task = Task(name=form.name.data, description=form.description.data, event_id=event.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully', 'success')
        return redirect(url_for('dashboard', event_name=event_name))

    return render_template('create_task.html', image_file=image_file, event=event, form=form)



@app.route('/create_event', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data, description=form.description.data,
                    location=form.location.data, date=form.date.data,
                    time=form.time.data, organizer=[current_user], managers=[current_user])
        if form.picture.data:
            picture_file = save_picture(form.picture.data, event=True)
            event.image_file = picture_file

        db.session.add(event)
        db.session.commit()
        flash('Event created successfully', 'success')
        return redirect(url_for('home'))

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    event_image_file = url_for('static', filename='event_pics/' + current_user.image_file)
    return render_template('create_event.html', image_file=image_file, event_image_file=event_image_file, form=form)


def save_picture(form_picture, event=False, new_width=800, new_height=800):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    path = 'static/profile_pics' if not event else 'static/event_pics'
    picture_path = os.path.join(app.root_path, path, picture_fn)
    output_size = (512, 512)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/profile', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def profile():
    """ Renders the dashboard page """
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', image_file=image_file, form=form)

@app.route('/test', strict_slashes=False)
def test():
    """ Renders the dashboard page """
    return render_template('test.html')
