from django.urls import path, include

urlpatterns = [
    path("", include("approval_engine.approval_tickets.drf_urls")),
    path("views/", include("approval_engine.approval_tickets.view_urls")),
]
