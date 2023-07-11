from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=200, null=True)
    address_2 = models.CharField(max_length=200, null=True)
