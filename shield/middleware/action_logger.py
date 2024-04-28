# action_logger.py

from django.utils.deprecation import MiddlewareMixin

from shield.models.alert import Alert

class ActionLoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Log every action, including views and downloads
        user = request.user
        if user.is_authenticated:
            action_message = f"User '{user.username}' accessed URL: {request.path}"
            Alert.objects.create(user=user, name="User Action", message=action_message)
