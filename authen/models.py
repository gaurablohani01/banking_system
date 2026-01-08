from django.db import models
from django.contrib.auth.models import AbstractUser
from authen.manager import UserManeger

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    phone_number= models.CharField(max_length=10, unique=True)
    email = models.EmailField(blank=False, unique=True)
    email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS=['email']

    objects = UserManeger()
