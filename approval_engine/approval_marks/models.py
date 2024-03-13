from django.db import models

# Create your models here.

ACTION_STATUS_CHOICES = (
    ('accept', 'Accept'),
    ('deny', 'Deny'),
    
)

class ApprovalMark(models.Model):
    
    action_status = models.CharField(max_length=255, choices=ACTION_STATUS_CHOICES)
    
    action_message = models.TextField(blank=True, null=True)
    
    attachment = models.FileField(upload_to="approval_attachments", blank=True, null=True)
    
    approval_level = models.OneToOneField('approval_levels.ApprovalLevel', on_delete=models.CASCADE, related_name="approval_mark")
    
    