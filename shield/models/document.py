from django.db import models
from accounts.models.user import CustomUser
from shield.models import BaseModel
from shield.models.folder import Folder


class Document(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.FileField(upload_to='documents/')
    encrypted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
