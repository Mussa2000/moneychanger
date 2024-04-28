# signals.py

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from shield.models.folder import Folder
from .models import Alert, Document
from django.utils import timezone
from datetime import timedelta

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    login_time = timezone.now() + timedelta(hours=2)
    action_message = f"User '{user.username}' logged in at {login_time}."
    Alert.objects.create(user=user, name="User Login", message=action_message)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logout_time = timezone.now() + timedelta(hours=2)
    action_message = f"User '{user.username}' logged out at {logout_time}. "
    Alert.objects.create(user=user, name="User Logout", message=action_message)

@receiver(post_save, sender=Document)
def log_document_creation_update(sender, instance, created, **kwargs):
    created_time = timezone.now() + timedelta(hours=2)
    if created:
        action_message = f"Document '{instance.name}' was created by user '{instance.created_by.username} at {created_time}'."
        Alert.objects.create(user=instance.created_by, name="Document Creation", message=action_message)
    else:
        action_message = f"Document '{instance.name}' was updated by user '{instance.created_by.username} at {created_time}'."
        Alert.objects.create(user=instance.created_by, name="Document Update", message=action_message)

@receiver(post_delete, sender=Document)
def log_document_deletion(sender, instance, **kwargs):
    deleted_time = timezone.now() + timedelta(hours=2)
    action_message = f"Document '{instance.name}' was deleted by user '{instance.created_by.username} at {deleted_time}'."
    Alert.objects.create(user=instance.created_by, name="Document Deletion", message=action_message)


@receiver(post_save, sender=Folder)
def log_folder_creation_update(sender, instance, created, **kwargs):
    created_time = timezone.now() + timedelta(hours=2)
    if created:
        action_message = f"Folder '{instance.name}' was created by user '{instance.user.username}' at {created_time}."
        Alert.objects.create(user=instance.user, name="Folder Creation", message=action_message)
    else:
        action_message = f"Folder '{instance.name}' was updated by user '{instance.user.username}' at {created_time}."
        Alert.objects.create(user=instance.user, name="Folder Update", message=action_message)

@receiver(post_delete, sender=Folder)
def log_folder_deletion(sender, instance, **kwargs):
    deleted_time = timezone.now() + timedelta(hours=2)
    action_message = f"Folder '{instance.name}' was deleted by user '{instance.user.username}' at {deleted_time}."
    Alert.objects.create(user=instance.user, name="Folder Deletion", message=action_message)

