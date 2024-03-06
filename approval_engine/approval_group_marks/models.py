from django.db import models

# Create your models here.


class ApprovalGroupMark(models.Model, ):
    
    action_status = models.CharField(max_length=255)
    
    action_message = models.CharField(max_length=255)
    
    approver = models.ForeignKey('approvers.Approver', on_delete=models.CASCADE, related_name="approval_group_marks")
    
    approval_group_level = models.ForeignKey('approval_group_levels.ApprovalGroupLevel', on_delete=models.CASCADE, related_name="approval_group_marks")
    
    