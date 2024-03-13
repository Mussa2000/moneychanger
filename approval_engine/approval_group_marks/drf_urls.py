from django.urls import path
from .drf_views import (
    ApprovalGroupMarkDeleteAPIView,
    ApprovalGroupMarkListAPIView,
    ApprovalGroupMarkCreateAPIView,
    ApprovalGroupMarkUpdateAPIView,
    ApprovalGroupMarkDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalGroupMarkListAPIView.as_view(), name="list-approval_group_marks"),
    path("detail/<int:pk>/", ApprovalGroupMarkDetailAPIView.as_view(), name="detail-approval_group_mark"),
    path("create/", ApprovalGroupMarkCreateAPIView.as_view(), name="create-approval_group_mark"),
    path("update/<int:pk>/", ApprovalGroupMarkUpdateAPIView.as_view(), name="update-approval_group_mark"),
    path("delete/<int:pk>/", ApprovalGroupMarkDeleteAPIView.as_view(), name="delete-approval_group_mark"),
]
