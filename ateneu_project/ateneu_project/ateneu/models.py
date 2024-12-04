from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Torna o e-mail único e obrigatório

    def __str__(self):
        return self.email  # Representa o usuário pelo e-mail
