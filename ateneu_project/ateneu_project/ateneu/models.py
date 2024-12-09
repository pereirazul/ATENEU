from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    nome_completo = models.CharField(max_length=255, verbose_name="Nome")
    def __str__(self):
         return self.nome_completo if self.nome_completo else self.email  
