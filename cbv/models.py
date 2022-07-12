from django.db import models

# Create your models here.


class fbvmodel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()


class ucbvmodel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()


class pcbvmodel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
