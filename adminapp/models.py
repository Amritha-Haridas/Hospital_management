from django.db import models

# Create your models here.

class Departmentsdb(models.Model):
    departmentname = models.CharField(max_length=30)
    profileimage = models.ImageField(upload_to = 'Image',default = "null.jpg")
    yearfounded = models.IntegerField()
    description = models.CharField(max_length=100)

class Logindb(models.Model):
    username = models.CharField(max_length=30)
    password=models.CharField(max_length=10,default='')