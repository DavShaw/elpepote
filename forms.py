# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TimeField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class DoctorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    specialty = SelectField('Specialty', choices=[
        ('general', 'General'),
        ('gynecology', 'Gynecology'),
        ('neurology', 'Neurology'),
        ('dentistry', 'Dentistry'),
        ('cardiology', 'Cardiology'),
        ('orthopedics', 'Orthopedics'),
        ('oncology', 'Oncology'),
        ('pediatrics', 'Pediatrics'),
        ('psychiatry', 'Psychiatry'),
        ('rheumatology', 'Rheumatology'),
        ('endocrinology', 'Endocrinology'),
        ('pulmonology', 'Pulmonology'),
        ('gastroenterology', 'Gastroenterology'),
        ('hematology', 'Hematology'),
        ('infectious_diseases', 'Infectious Diseases'),
        ('nephrology', 'Nephrology'),
        ('ophthalmology', 'Ophthalmology'),
        ('otolaryngology', 'Otolaryngology'),
        ('urology', 'Urology'),
        ('allergy_and_immunology', 'Allergy and Immunology'),
        ('anesthesiology', 'Anesthesiology'),
        ('emergency_medicine', 'Emergency Medicine'),
        ('medical_genetics', 'Medical Genetics'),
        ('internal_medicine', 'Internal Medicine'),
        ('radiology', 'Radiology'),
        ('surgery', 'Surgery'),
        ('trauma', 'Trauma')
    ], validators=[DataRequired()])
    dni = IntegerField('DNI', validators=[DataRequired()])
    submit = SubmitField('Add Doctor')

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    dni = StringField('dni', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class AppointmentForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()])
    reason = TextAreaField('Reason', validators=[DataRequired()])
    doctor_id = SelectField('Doctor', coerce=int)
    patient_id = SelectField('Patient', coerce=int)

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    dni = StringField('dni', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    dni = StringField('DNI', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class TwoFactorForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired()])