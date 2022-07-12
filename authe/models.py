from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class registermodel(User):
    phone = models.PositiveBigIntegerField()
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, choices=[
                              ['Male', 'Male'], ['Female', 'Female']])
    dob = models.DateField()
    img = models.ImageField(upload_to='profile/')
