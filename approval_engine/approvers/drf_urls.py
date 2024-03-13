from django.urls import path
from .drf_views import (
    ApproverDeleteAPIView,
    ApproverListAPIView,
    ApproverCreateAPIView,
    ApproverUpdateAPIView,
    ApproverDetailAPIView
)


urlpatterns = [
    path("list/", ApproverListAPIView.as_view(), name="list-approvers"),
    path("detail/<int:pk>/", ApproverDetailAPIView.as_view(), name="detail-approver"),
    path("create/", ApproverCreateAPIView.as_view(), name="create-approver"),
    path("update/<int:pk>/", ApproverUpdateAPIView.as_view(), name="update-approver"),
    path("delete/<int:pk>/", ApproverDeleteAPIView.as_view(), name="delete-approver"),
]
