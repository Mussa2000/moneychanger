from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    
    