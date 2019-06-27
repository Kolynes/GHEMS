from django.db import models
from utils.models import PasswordField
from utils.choices import MARITAL_STATUSES, GENDERS, COUNTRIES

class Patient(models.Model):
    hashcode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    occupation = models.TextField()
    address = models.TextField()
    marital = models.CharField("Marital Status", max_length=1, choices=MARITAL_STATUSES)
    sex = models.CharField(max_length=1, choices=GENDERS)
    age = models.IntegerField()
    phone = models.CharField(max_length=14)
    nationality = models.CharField(max_length=2, choices=COUNTRIES)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    date = models.DateTimeField("Date of registration", auto_now_add=True)
    passcode = PasswordField()

class History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    report = models.TextField()
    date = models.DateTimeField("Date of report", auto_now_add=True)
    diagnosis = models.TextField()
    prescription = models.TextField()

class Hospital(models.Model):
    name = models.TextField()
    address = models.TextField()
    code = models.TextField("Hospital Registration Code")
    passcode = PasswordField()
