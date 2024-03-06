from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Approver(models.Model, ):
    
    user = models.ForeignKey(get_user_model(), related_name="approver", on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f'{self.user}'

class ApproverProxy(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='approver_proxy', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'