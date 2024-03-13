from django.urls import path, include

urlpatterns = [
    path("", include("approval_engine.approval_actions.drf_urls")),
    path("views/", include("approval_engine.approval_actions.view_urls")),
]
