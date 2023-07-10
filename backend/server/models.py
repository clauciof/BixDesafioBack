from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True, primary_key=True)
    addres = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    type = models.CharField(max_length=10)
    entry =  models.DateField(default=datetime.date.today)
    out =  models.DateField(default=datetime.date.today)
    holidays =  models.DateField(default=datetime.date.today)

