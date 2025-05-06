from django.db import models

from exchange_rate.models import ExchangeAgreement

class TradeChatRoom(models.Model):
    agreement = models.ForeignKey(ExchangeAgreement, on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}..."