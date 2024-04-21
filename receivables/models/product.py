from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    unit_cost = models.FloatField(default=0.00)
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    
    