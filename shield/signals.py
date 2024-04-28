# signals.py

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Alert, Document

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    action_message = f"User '{user.username}' logged in."
    Alert.objects.create(user=user, name="User Login", message=action_message)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    action_message = f"User '{user.username}' logged out. "
    Alert.objects.create(user=user, name="User Logout", message=action_message)

@receiver(post_save, sender=Document)
def log_document_creation_update(sender, instance, created, **kwargs):
    if created:
        action_message = f"Document '{instance.name}' was created by user '{instance.created_by.username} at {instance.created_at}'."
        Alert.objects.create(user=instance.created_by, name="Document Creation", message=action_message)
    else:
        action_message = f"Document '{instance.name}' was updated by user '{instance.created_by.username} at {instance.created_at}'."
        Alert.objects.create(user=instance.created_by, name="Document Update", message=action_message)

@receiver(post_delete, sender=Document)
def log_document_deletion(sender, instance, **kwargs):
    action_message = f"Document '{instance.name}' was deleted by user '{instance.created_by.username} at {instance.created_at}'."
    Alert.objects.create(user=instance.created_by, name="Document Deletion", message=action_message)

# You can extend this pattern to capture download actions if needed
