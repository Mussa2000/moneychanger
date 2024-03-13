from django.db import models

# Create your models here.


class ApprovalGroupAction(models.Model, ):
    
    name = models.CharField(max_length=255)
    
    description = models.CharField(max_length=255)
    
    module_to_execute_location = models.CharField(max_length=255)
    
    ...

class ApprovalGroupActionProxy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    module_to_execute_location = models.CharField(max_length=255)