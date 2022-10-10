from django.db import models
from django.forms import ModelForm

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=50)



