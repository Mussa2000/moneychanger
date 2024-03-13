from django.urls import path
from .drf_views import (
    ApprovalGroupDeleteAPIView,
    ApprovalGroupListAPIView,
    ApprovalGroupCreateAPIView,
    ApprovalGroupUpdateAPIView,
    ApprovalGroupDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalGroupListAPIView.as_view(), name="list-approval_groups"),
    path("detail/<int:pk>/", ApprovalGroupDetailAPIView.as_view(), name="detail-approval_group"),
    path("create/", ApprovalGroupCreateAPIView.as_view(), name="create-approval_group"),
    path("update/<int:pk>/", ApprovalGroupUpdateAPIView.as_view(), name="update-approval_group"),
    path("delete/<int:pk>/", ApprovalGroupDeleteAPIView.as_view(), name="delete-approval_group"),
]
