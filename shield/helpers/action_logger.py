from django.utils import timezone
from datetime import timedelta
from shield.models.alert import Alert

def log_action(user, action_name, target_name, target_user=None):
    timestamp = timezone.now() + timedelta(hours=2)
    if user:
        message = f"{action_name} '{target_name}' by user '{user.username}' at {timestamp}."
    else:
        message = f"{action_name} '{target_name}' at {timestamp}."
    Alert.objects.create(user=user, name=action_name, message=message)
