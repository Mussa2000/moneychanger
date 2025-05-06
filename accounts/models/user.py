from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from exchange_rate.models import Currency

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


class KYCProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=100)
    residential_address = models.TextField()
    is_verified = models.BooleanField(default=False)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField(upload_to='kyc_documents/', null=True, blank=True)

    def __str__(self):
        return f"KYC Profile - {self.user.username}"
