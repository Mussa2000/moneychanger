from django.urls import path, include
from . import views
from accounts.views import CustomPasswordResetView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # user authentication
     path("", include("allauth.urls")),
]
