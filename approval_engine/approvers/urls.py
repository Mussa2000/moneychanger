from django.urls import path, include

urlpatterns = [
    path("", include("approval_engine.approvers.drf_urls")),
    path("views/", include("approval_engine.approvers.view_urls")),
]
