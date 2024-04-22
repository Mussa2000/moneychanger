from django.db import models
from accounts.models.user import CustomUser
from receivables.models import Transaction
from receivables.models.bank import Bank

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True, blank=True)
    pay_date = models.DateField()
    amount = models.FloatField(default=0.00)
    payment_type = models.CharField(max_length=10, default='Bank', choices=STATUS_CHOICES, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.pay_date}'
    
    def total(self):
        return self.quantity * self.product.unit_cost

    
    