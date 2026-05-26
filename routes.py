from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db
from models import User, Donation, Volunteer, Campaign, Event
from forms import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash('Registration Successful')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))

        flash('Invalid Credentials')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/dashboard')
@login_required
def dashboard():
    donations = Donation.query.all()
    volunteers = Volunteer.query.all()
    campaigns = Campaign.query.all()
    events = Event.query.all()

    total_donation = sum([d.amount for d in donations])

    return render_template(
        'dashboard.html',
        donations=donations,
        volunteers=volunteers,
        campaigns=campaigns,
        events=events,
        total_donation=total_donation
    )

@app.route('/donations')
@login_required
def donations():
    all_donations = Donation.query.all()
    return render_template('donations.html', donations=all_donations)

@app.route('/add_donation', methods=['GET', 'POST'])
@login_required
def add_donation():
    form = DonationForm()

    if form.validate_on_submit():
        donation = Donation(
            donor_name=form.donor_name.data,
            amount=form.amount.data,
            purpose=form.purpose.data
        )

        db.session.add(donation)
        db.session.commit()

        flash('Donation Added Successfully')
        return redirect(url_for('donations'))

    return render_template('add_donation.html', form=form)


@app.route('/volunteers')
@login_required
def volunteers():
    all_volunteers = Volunteer.query.all()
    return render_template('volunteers.html', volunteers=all_volunteers)

@app.route('/add_volunteer', methods=['GET', 'POST'])
@login_required
def add_volunteer():
    form = VolunteerForm()

    if form.validate_on_submit():
        volunteer = Volunteer(
            name=form.name.data,
            phone=form.phone.data,
            skills=form.skills.data
        )

        db.session.add(volunteer)
        db.session.commit()

        flash('Volunteer Added')
        return redirect(url_for('volunteers'))

    return render_template('add_volunteer.html', form=form)

@app.route('/campaigns')
@login_required
def campaigns():
    all_campaigns = Campaign.query.all()
    return render_template('campaigns.html', campaigns=all_campaigns)

@app.route('/add_campaign', methods=['GET', 'POST'])
@login_required
def add_campaign():
    form = CampaignForm()

    if form.validate_on_submit():
        campaign = Campaign(
            title=form.title.data,
            description=form.description.data,
            target_amount=form.target_amount.data
        )

        db.session.add(campaign)
        db.session.commit()

        flash('Campaign Added')
        return redirect(url_for('campaigns'))

    return render_template('add_campaign.html', form=form)


@app.route('/events')
#@login_required
def events():
    all_events = Event.query.all()
    return render_template('events.html', events=all_events)


@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    form = EventForm()

    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            location=form.location.data,
            date=form.date.data
        )

        db.session.add(event)
        db.session.commit()

        flash('Event Added')
        return redirect(url_for('events'))

    return render_template('add_event.html', form=form)