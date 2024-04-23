from django.contrib.auth.models import AbstractUser
from django.db import models
from receivables.models.province import Province

class CustomUser(AbstractUser):
    province = models.ForeignKey('receivables.Province', on_delete=models.PROTECT, null=True, blank=True)
    is_farmer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
