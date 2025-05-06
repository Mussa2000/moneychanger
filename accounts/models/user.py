from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('Trader', 'Trader'),
        ('Regulator', 'Regulator'),
    ]

    user_role = models.CharField(
        max_length=50,
        choices=USER_ROLE_CHOICES,
        default='Trader'
    )

    def __str__(self):
        return f"{self.username} ({self.user_role})"
    
    def save(self, *args, **kwargs):
        if not self.date_joined:
            self.date_joined = timezone.now()
        super().save(*args, **kwargs)
