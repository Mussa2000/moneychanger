from django.urls import path
from .drf_views import (
    ApprovalLevelDeleteAPIView,
    ApprovalLevelListAPIView,
    ApprovalLevelCreateAPIView,
    ApprovalLevelUpdateAPIView,
    ApprovalLevelDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalLevelListAPIView.as_view(), name="list-approval_levels"),
    path("detail/<int:pk>/", ApprovalLevelDetailAPIView.as_view(), name="detail-approval_level"),
    path("create/", ApprovalLevelCreateAPIView.as_view(), name="create-approval_level"),
    path("update/<int:pk>/", ApprovalLevelUpdateAPIView.as_view(), name="update-approval_level"),
    path("delete/<int:pk>/", ApprovalLevelDeleteAPIView.as_view(), name="delete-approval_level"),
]
