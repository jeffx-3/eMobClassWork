from django.db import models

# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=4)
    yob = models.DateField()
    
    def __str__(self):
        return self.fullname

#user register

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    