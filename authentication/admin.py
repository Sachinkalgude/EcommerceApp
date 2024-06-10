from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(Users)
class UserModelAdmin(UserAdmin):
    list_display = ('id','email','first_name','adress')
    