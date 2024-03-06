from django.urls import path
from .drf_views import (
    ApprovalActionDeleteAPIView,
    ApprovalActionListAPIView,
    ApprovalActionCreateAPIView,
    ApprovalActionUpdateAPIView,
    ApprovalActionDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalActionListAPIView.as_view(), name="list-approval_actions"),
    path("detail/<int:pk>/", ApprovalActionDetailAPIView.as_view(), name="detail-approval_action"),
    path("create/", ApprovalActionCreateAPIView.as_view(), name="create-approval_action"),
    path("update/<int:pk>/", ApprovalActionUpdateAPIView.as_view(), name="update-approval_action"),
    path("delete/<int:pk>/", ApprovalActionDeleteAPIView.as_view(), name="delete-approval_action"),
]
