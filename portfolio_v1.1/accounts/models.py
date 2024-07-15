from django.db import models
from django.contrib.auth.models import User
from pages.models import Company
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __self__(self):
        return f"{self.user.username}"
    
