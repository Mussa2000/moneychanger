from django.db import models

# Create your models here.


class ApprovalLevel(models.Model, ):
    
    index = models.IntegerField()
    
    name = models.CharField(max_length=255)
    
    approver = models.ForeignKey('approvers.Approver', on_delete=models.CASCADE, related_name="approval_levels")
    
    approval_group = models.ForeignKey('approval_groups.ApprovalGroup', on_delete=models.CASCADE, related_name="approval_levels")
    
    ...

class ApprovalLevelProxy(models.Model):
    
    index = models.IntegerField()
    
    name = models.CharField(max_length=255)
    
    approver = models.ForeignKey('approvers.ApproverProxy', on_delete=models.CASCADE, related_name="approval_levels")
    
    approval_group = models.ForeignKey('approval_groups.ApprovalGroupProxy', on_delete=models.CASCADE, related_name="approval_levels")