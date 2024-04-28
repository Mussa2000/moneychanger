from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.date_joined:
            self.date_joined = timezone.now()
        super().save(*args, **kwargs)

