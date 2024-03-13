from django.db import models

# Create your models here.


class ApprovalGroupLevel(models.Model, ):
    
    name = models.CharField(max_length=255)
    
    index = models.IntegerField()
    
    approval_group = models.ForeignKey('approval_groups.ApprovalGroup', on_delete=models.CASCADE, related_name='approval_group_levels')
    
    approval_ticket = models.ForeignKey('approval_tickets.ApprovalTicket', on_delete=models.CASCADE, related_name='approval_group_levels')
    
    ...

class ApprovalGroupLevelProxy(models.Model, ):
    
    name = models.CharField(max_length=255)
    
    index = models.IntegerField()
    
    approval_group = models.ForeignKey('approval_groups.ApprovalGroupProxy', on_delete=models.CASCADE, related_name='approval_group_levels')
    
    approval_ticket = models.ForeignKey('approval_tickets.ApprovalTicketProxy', on_delete=models.CASCADE, related_name='approval_group_levels')
    
    ...

