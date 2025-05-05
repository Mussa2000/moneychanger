from django.db import models

class Currency(models.Model):
    """
    Represents a currency like USD, ZWL, EUR, etc.
    """
    country = models.CharField(max_length=100, null=True, blank=True)             # e.g., 'United States', 'Zimbabwe'
    code = models.CharField(max_length=10, unique=True)  # e.g., 'USD', 'ZWL'
    name = models.CharField(max_length=50)               # e.g., 'United States Dollar'

    def __str__(self):
        return f"{self.name} ({self.code})"


class ExchangeSource(models.Model):
    """
    Represents the source of the exchange rate, like RBZ, Street Rate, etc.
    """
    name = models.CharField(max_length=100, unique=True)   # e.g., 'RBZ', 'Parallel Market'
    description = models.TextField(blank=True, null=True)

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

    class Meta:
        unique_together = ('base_currency', 'target_currency', 'source', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} | 1 {self.base_currency.code} = {self.rate} {self.target_currency.code} ({self.source})"
