from django.contrib.auth.models import BaseUserManager
from .models import *

class usermanager(BaseUserManager):
    def crete_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('the email is required!')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        return self.crete_user(email,password,**extra_fields)
    