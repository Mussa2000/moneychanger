from django.db import models

# Create your models here.

class ApprovalAction(models.Model):
    
    name = models.CharField(max_length=255)
    
    description = models.TextField()
    
    module_to_execute_location = models.CharField(max_length=255)
    
    code = models.CharField(max_length=255, default='ROC')
    
    def __str__(self) -> str:
        return f'{self.name} : {self.code}'

class ApprovalActionProxy(models.Model):
    name = models.CharField(max_length=255)
    
    description = models.TextField()
    
    module_to_execute_location = models.CharField(max_length=255)
    
    code = models.CharField(max_length=255, default='ROC')