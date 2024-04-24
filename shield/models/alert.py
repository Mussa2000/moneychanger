from django.db import models
from accounts.models.user import CustomUser
from shield.models import BaseModel
from shield.models.folder import Folder


class Alert(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} Alert"
