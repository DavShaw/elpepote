# models.py
from enum import Enum
from sqlalchemy import Enum as SqlEnum
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta
from wtforms.validators import DataRequired
from wtforms import DateField, TimeField, TextAreaField, SelectField

db = SQLAlchemy()

def date_today_plus_one():
    return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
def time_now_plus_one():
    return (datetime.now() + timedelta(hours=1)).strftime('%H:%M')


class SpecialtyEnum(Enum):
    general = 'general'
    gynecology = 'gynecology'
    neurology = 'neurology'
    dentistry = 'dentistry'
    cardiology = 'cardiology'
    orthopedics = 'orthopedics'
    oncology = 'oncology'
    pediatrics = 'pediatrics'
    psychiatry = 'psychiatry'
    rheumatology = 'rheumatology'
    endocrinology = 'endocrinology'
    pulmonology = 'pulmonology'
    gastroenterology = 'gastroenterology'
    hematology = 'hematology'
    infectious_diseases = 'infectious diseases'
    nephrology = 'nephrology'
    ophthalmology = 'ophthalmology'
    otolaryngology = 'otolaryngology'
    urology = 'urology'
    allergy_and_immunology = 'allergy and immunology'
    anesthesiology = 'anesthesiology'
    emergency_medicine = 'emergency medicine'
    medical_genetics = 'medical genetics'
    internal_medicine = 'internal medicine'
    radiology = 'radiology'
    surgery = 'surgery'
    trauma = 'trauma'


class Doctor(db.Model):
    __tablename__ = 'doctor'
    dni = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    specialty = db.Column(SqlEnum(SpecialtyEnum), nullable=False)


class Patient(db.Model, UserMixin):
    dni = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=False)

    def get_id(self):
        return self.dni
    
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.dni'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.dni'), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id}>'
