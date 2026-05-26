from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class DonationForm(FlaskForm):
    donor_name = StringField('Donor Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    purpose = StringField('Purpose')
    submit = SubmitField('Add Donation')

class VolunteerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone')
    skills = StringField('Skills')
    submit = SubmitField('Add Volunteer')


class CampaignForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    target_amount = FloatField('Target Amount')
    submit = SubmitField('Add Campaign')


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    location = StringField('Location')
    date = StringField('Date')
    submit = SubmitField('Add Event')