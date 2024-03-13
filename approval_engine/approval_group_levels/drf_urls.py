from django.urls import path
from .drf_views import (
    ApprovalGroupLevelDeleteAPIView,
    ApprovalGroupLevelListAPIView,
    ApprovalGroupLevelCreateAPIView,
    ApprovalGroupLevelUpdateAPIView,
    ApprovalGroupLevelDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalGroupLevelListAPIView.as_view(), name="list-approval_group_levels"),
    path("detail/<int:pk>/", ApprovalGroupLevelDetailAPIView.as_view(), name="detail-approval_group_level"),
    path("create/", ApprovalGroupLevelCreateAPIView.as_view(), name="create-approval_group_level"),
    path("update/<int:pk>/", ApprovalGroupLevelUpdateAPIView.as_view(), name="update-approval_group_level"),
    path("delete/<int:pk>/", ApprovalGroupLevelDeleteAPIView.as_view(), name="delete-approval_group_level"),
]
