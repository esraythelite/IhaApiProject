from django.db import models

# Create your models here.

#user 
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=100,default='123')

#iha
class Iha(models.Model):
    IhaId = models.AutoField(primary_key=True)
    IhaBrand = models.CharField(max_length=150)
    IhaModel = models.CharField(max_length=200)
    IhaCategory = models.CharField(max_length=150)
    IhaWeight = models.BigIntegerField()
    IhaLength = models.BigIntegerField()
    IhaProductionDate = models.DateField()
    IhaPhotoFileName = models.CharField(max_length=500)
