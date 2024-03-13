from django.db import models

# Create your models here.


class ApprovalGroup(models.Model, ):
    
    name = models.CharField(max_length=255)
    approval_ticket = models.ForeignKey('approval_tickets.ApprovalTicket', on_delete=models.CASCADE, related_name="approval_groups")
    
    def __str__(self):
        return self.name
    
    def ordered_approval_levels(self):
        return self.approval_levels.all().order_by('index')
    

class ApprovalGroupProxy(models.Model):
    name = models.CharField(max_length=255)
    approval_ticket = models.ForeignKey('approval_tickets.ApprovalTicketProxy', on_delete=models.CASCADE, related_name="approval_group_proxies")
    
    def __str__(self):
        return self.name
    def ordered_approval_levels(self):
        return self.approval_levels.all().order_by('index')