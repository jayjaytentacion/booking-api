from imghdr import what
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username=None
    last_name=None
    first_name=None
    full_name=models.CharField(max_length=28,null=True)
    phone_number=models.IntegerField(unique=True,null=True)
    email=models.EmailField(unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    class Meta:
        ordering=['-email']
        verbose_name='User'

    # def __str__(self):
    #     return self.full_name    


class Bookee(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    full_name=models.CharField(max_length=28,null=True)
    phone_number=models.IntegerField(unique=True,null=True) 
         

    # def __str__(self):
    #     return self.full_name  