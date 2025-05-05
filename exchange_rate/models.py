from django.db import models

class Currency(models.Model):
    """
    Represents a currency like USD, ZWL, EUR, etc.
    """
    country = models.CharField(max_length=100, null=True, blank=True)             # e.g., 'United States', 'Zimbabwe'
    code = models.CharField(max_length=10, unique=True)  # e.g., 'USD', 'ZWL'
    name = models.CharField(max_length=50)               # e.g., 'United States Dollar'
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class ExchangeSource(models.Model):
    """
    Represents the source of the exchange rate, like RBZ, Street Rate, etc.
    """
    name = models.CharField(max_length=100, unique=True)   # e.g., 'RBZ', 'Parallel Market'
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    """
    Stores exchange rate data between two currencies from a specific source on a specific date.
    """
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_rates')
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='target_rates')
    rate = models.DecimalField(max_digits=20, decimal_places=6)  # e.g., 15500.00
    source = models.ForeignKey(ExchangeSource, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        unique_together = ('base_currency', 'target_currency', 'source', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} | 1 {self.base_currency.code} = {self.rate} {self.target_currency.code} ({self.source})"


class Transaction(models.Model):
    """
    Represents a currency exchange transaction.
    """
    TRANSACTION_TYPE_CHOICES = [
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
        ('Transfer', 'Transfer'),
    ]

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default='Buy'
    )
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_transactions')
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='target_transactions')
    amount = models.DecimalField(max_digits=20, decimal_places=2) 
    rate = models.ForeignKey(ExchangeRate, on_delete=models.SET_NULL, null=True)
    received_amount = models.DecimalField(max_digits=20, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} | {self.amount} {self.base_currency.code} -> {self.rate} {self.target_currency.code} ({self.rate})"