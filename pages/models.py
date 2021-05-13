from django.db import models
from datetime import datetime, timezone
from django.utils import timezone

# Create your models here.

class admin_model(models.Model):
    advisor_name = models.CharField(max_length=100)
    advisor_image = models.ImageField(upload_to='static/images/',blank=True,default="")
    advisor_id = models.IntegerField(default=0)
    
    def __str__(self):
        return self.advisor_name
    
class user_models(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class login_user(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.email

class can_book_call(models.Model):
    date = models.DateField(default=timezone.now)
    booking_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.booking_id
    
class all_book_call(models.Model):
    advisor_name = models.CharField(max_length=100,default=1)
    advisor_image = models.CharField(max_length=100,blank=True)
    advisor_id = models.CharField(max_length=100,default=1)
    date = models.DateField(default=timezone.now)
    booking_id = models.CharField(max_length=100,default=1)
    
    def __str__(self):
        return self.advisor_name