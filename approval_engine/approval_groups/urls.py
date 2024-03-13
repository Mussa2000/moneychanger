from django.urls import path, include

urlpatterns = [
    path("", include("approval_engine.approval_groups.drf_urls")),
    path("views/", include("approval_engine.approval_groups.view_urls")),
]
