# models.py
from enum import Enum
from sqlalchemy import Enum as SqlEnum
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class SpecialtyEnum(Enum):
    GENERAL = 'general'
    GYNECOLOGY = 'gynecology'
    NEUROLOGY = 'neurology'
    DENTISTRY = 'dentistry'
    CARDIOLOGY = 'cardiology'
    ORTHOPEDICS = 'orthopedics'
    ONCOLOGY = 'oncology'
    PEDIATRICS = 'pediatrics'
    PSYCHIATRY = 'psychiatry'
    RHEUMATOLOGY = 'rheumatology'
    ENDOCRINOLOGY = 'endocrinology'
    PULMONOLOGY = 'pulmonology'
    GASTROENTEROLOGY = 'gastroenterology'
    HEMATOLOGY = 'hematology'
    INFECTIOUS_DISEASES = 'infectious diseases'
    NEPHROLOGY = 'nephrology'
    OPHTHALMOLOGY = 'ophthalmology'
    OTOLARYNGOLOGY = 'otolaryngology'
    UROLOGY = 'urology'
    ALLERGY_AND_IMMUNOLOGY = 'allergy and immunology'
    ANESTHESIOLOGY = 'anesthesiology'
    EMERGENCY_MEDICINE = 'emergency medicine'
    MEDICAL_GENETICS = 'medical genetics'
    INTERNAL_MEDICINE = 'internal medicine'
    RADIOLOGY = 'radiology'
    SURGERY = 'surgery'
    TRAUMA = 'trauma'


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
    reason = db.Column(db.Text, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.dni'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.dni'), nullable=False)

    doctor = db.relationship('Doctor', backref='appointments')
    patient = db.relationship('Patient', backref='appointments')
