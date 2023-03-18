from django.db import models

# Create your models here.
class Headdb(models.Model):
    name = models.CharField(max_length=30)
    images = models.ImageField(upload_to = 'Image',default = "null.jpg")
    age = models.IntegerField()
    number = models.CharField(max_length=30)
    des = models.CharField(max_length=30)
    report = models.CharField(max_length=30,default="")

class Employeedb(models.Model):
    ename = models.CharField(max_length=30)
    eimages = models.ImageField(upload_to = 'Image',default = "null.jpg")
    eage = models.IntegerField()
    enumber = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)    
    report = models.CharField(max_length=30,default="")    