from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", include("allauth.urls")),
]
