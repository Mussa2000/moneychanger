from django.db import models

from accounts.models.user import CustomUser
from receivables.models.product import Product

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    tra_date = models.DateField()
    quantity= models.IntegerField(default =1)
    description = models.CharField(max_length=255)
    amount_paid = models.FloatField(null=True, blank=True, default=0.00)
    status = models.CharField(max_length=10, default='pending', choices=STATUS_CHOICES, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.tra_date}'
    
    def total(self):
        return self.quantity * self.product.unit_cost

    
    