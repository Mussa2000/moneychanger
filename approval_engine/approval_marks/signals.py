from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from approval_engine.approval_group_marks.models import ApprovalGroupMark
from .models import ApprovalMark


@receiver(post_save, sender=ApprovalMark)
def notify_the_next_approver_on_creation(sender, instance: ApprovalMark, created, **kwargs):
    if created:
        # if the status is denied then proceed to mark the ticket as revoked and execute actions
        if instance.action_status == 'deny':
            approval_ticket = instance.approval_level.approval_group.approval_ticket
            ApprovalGroupMark.objects.create(
                action_status=instance.action_status,
                approval_group_level=instance.approval_level.approval_group.approval_group_levels.first(),
                action_message=instance.action_message,
                approver=instance.approval_level.approver,
            )
            approval_ticket.execute_actions()
            settings.LOGGER.warning(f'Ending Execution For {approval_ticket}')
            return 
            ...
        # find the next approval level and notify that use
        approval_levels_in_group_without_approval_marks = (
            instance.approval_level.approval_group.approval_levels.filter(
                approval_mark__isnull=True
            ).order_by('index')
        )
        
        # if the levels are empty then proceed to the next group
        if approval_levels_in_group_without_approval_marks.count() == 0:
            settings.LOGGER.debug(f'Creating Group Mark for {instance.approval_level.approval_group}')
            ApprovalGroupMark.objects.create(
                action_status=instance.action_status,
                approval_group_level=instance.approval_level.approval_group.approval_group_levels.first(),
                action_message=instance.action_message,
                approver=instance.approval_level.approver,
            )
            
        else:
            next_approval_level = approval_levels_in_group_without_approval_marks.first()
            settings.LOGGER.debug(f"Notifying {next_approval_level.index} {next_approval_level.approver}")
            
            
            ...
        # else notify the next level approver 
        
