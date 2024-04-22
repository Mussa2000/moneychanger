from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model
from django.urls import resolve

@receiver(user_signed_up, sender=get_user_model())
def set_user_is_farmer(sender, request, user, **kwargs):
    # Get the resolved URL name from the request
    resolved_url_name = resolve(request.path_info).url_name
    
    # Check if the signup is coming from the specific URL
    if resolved_url_name == 'account_signup':
        user.is_farmer = True
        user.save()
