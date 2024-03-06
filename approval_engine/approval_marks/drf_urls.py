from django.urls import path
from .drf_views import (
    ApprovalMarkDeleteAPIView,
    ApprovalMarkListAPIView,
    ApprovalMarkCreateAPIView,
    ApprovalMarkUpdateAPIView,
    ApprovalMarkDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalMarkListAPIView.as_view(), name="list-approval_marks"),
    path("detail/<int:pk>/", ApprovalMarkDetailAPIView.as_view(), name="detail-approval_mark"),
    path("create/", ApprovalMarkCreateAPIView.as_view(), name="create-approval_mark"),
    path("update/<int:pk>/", ApprovalMarkUpdateAPIView.as_view(), name="update-approval_mark"),
    path("delete/<int:pk>/", ApprovalMarkDeleteAPIView.as_view(), name="delete-approval_mark"),
]
