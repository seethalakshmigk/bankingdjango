from django.db import models

class User_Table(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password=models.TextField(max_length=100)

class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    materials_provide = models.CharField(max_length=100)


