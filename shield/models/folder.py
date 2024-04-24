from django.db import models
from accounts.models.user import CustomUser
from shield.models import BaseModel


class Folder(BaseModel):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(CustomUser, null=True, blank=True)

    def __str__(self):
        return self.name