from django.db import models
from django import forms

# Create your models here.

GENDER_CHOICES = (
    ('male','MALE'),
    ('female','FEMALE'),
    ('others','OTHERS')
)
PAYMENT_CHOICES = (
    ('Cash','CASH'),
    ('Credit Card','CREDIT CARD'),
    ('Debit Card','DEBIT CARD'),
    ('UPI','UPI')
)
ROOM_CHOICES = (
    ('1001','1001(1 bed)'),
    ('1002','1002(2 beds)'),
    ('1003','1003(3 beds)'),
    ('1004','1004(4 beds)'),
    ('2001','2001(1 bed)'),
    ('2002','2002(2 beds)')
)

class CheckInModel(models.Model):
    id = models.AutoField(primary_key=True) 
    first_name = models.CharField(default = None,max_length=30)
    last_name = models.CharField(default = None,max_length=30)
    email = models.EmailField(default = None,max_length=254)
    age = models.IntegerField(default = None)
    address = models.TextField(default = None,max_length=250)
    gender = models.CharField(default = None,choices=GENDER_CHOICES, max_length=10)
    payment_method = models.CharField(default = None, choices=PAYMENT_CHOICES,max_length=20)
    file_field = models.ImageField(db_column='Poi_Img',upload_to='')
    checkin = models.DateField(default = None)
    checkout = models.DateField(default = None)
    room_allocated = models.CharField(default = None,choices=ROOM_CHOICES,max_length=100)
    additional_choices = models.CharField(default = None,max_length=100)