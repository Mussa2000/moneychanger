from django.urls import path, include

urlpatterns = [
    path("", include("approval_engine.approval_group_marks.drf_urls")),
    path("views/", include("approval_engine.approval_group_marks.view_urls")),
]
