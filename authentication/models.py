from django.db import models
from django.contrib.auth.models import AbstractUser
from .usermanager import *
# Create your models here.

class Users(AbstractUser):
    username = models.CharField(max_length=26)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    middel_name = models.CharField(max_length=26)
    dob = models.DateTimeField(null=True,blank=True)
    adress = models.TextField()
    
    created_at = models.DateTimeField(auto_now=True)
    updtaed_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = usermanager()
    
    def __str__(self):
        return f"{self.email}-{self.first_name}-{self.adress}"