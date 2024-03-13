from django.urls import path, include

urlpatterns = [
    path("", include("approval_engine.approval_levels.drf_urls")),
    path("views/", include("approval_engine.approval_levels.view_urls")),
]
