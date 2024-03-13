import time
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.sites.models import Site
from helpers.email_helpers import send_email_with_attachments
from .models import ApprovalGroupMark
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

@receiver(post_save, sender=ApprovalGroupMark)
def notify_the_next_group_on_creation(sender, instance: ApprovalGroupMark, created, **kwargs):
    if created:
        # if the group mark is denied then stop execution here 
        if instance.action_status == 'deny':
            settings.LOGGER.warning('Ending workflow because of denied Group Mark')
            return 
        # fetch the next group level
        higher_group_levels = (
            instance.approval_group_level.approval_group.approval_ticket.approval_group_levels.filter(
                index__gt=instance.approval_group_level.index
            ).order_by('index')
        )
        if higher_group_levels.count() == 0:
            settings.LOGGER.debug('All groups have submitted reviews')
            settings.LOGGER.info('Executing Actions')
            approval_ticket = instance.approval_group_level.approval_group.approval_ticket
            approval_ticket.execute_actions()
            ...
        else:
            # notify the first approver 
            next_group_level = higher_group_levels.first()
            settings.LOGGER.debug(f"Notifying first approver {next_group_level.approval_group.ordered_approval_levels().first().approver} of group {next_group_level.approval_group}")
            next_level = next_group_level.approval_group.approval_levels.all().order_by('index').first()
            next_approver = next_level.approver
            # send email notification to the next approver
            subject = f'Approval Required - {instance.approval_group_level.approval_group.approval_ticket.get_action_model()}'
            payload = {
                'next_approver' : next_approver,
                'approval_ticket' : next_level.approval_group.approval_ticket,
                'next_group_level' : next_group_level,
                'current_date' : str(time.ctime()),
                'site' : Site.objects.first()
            }
            message = render_to_string('approval_emails/notify_next_approver.html', payload)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [next_approver.user.email,]

            # Send the email
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                html_message=message,
                recipient_list=to_email,
                auth_user='apps@oacey.com',
                auth_password='@lkM$][=s68&&-2023',
            )
            
            
            
            
            
