from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email=models.CharField(max_length=100, null=True, blank=True)
    senha=models.CharField(max_length=100, null=True, blank=True)
def __str__(self):
    return self