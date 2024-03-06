from django.urls import path
from .drf_views import (
    ApprovalGroupActionDeleteAPIView,
    ApprovalGroupActionListAPIView,
    ApprovalGroupActionCreateAPIView,
    ApprovalGroupActionUpdateAPIView,
    ApprovalGroupActionDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalGroupActionListAPIView.as_view(), name="list-approval_group_actions"),
    path("detail/<int:pk>/", ApprovalGroupActionDetailAPIView.as_view(), name="detail-approval_group_action"),
    path("create/", ApprovalGroupActionCreateAPIView.as_view(), name="create-approval_group_action"),
    path("update/<int:pk>/", ApprovalGroupActionUpdateAPIView.as_view(), name="update-approval_group_action"),
    path("delete/<int:pk>/", ApprovalGroupActionDeleteAPIView.as_view(), name="delete-approval_group_action"),
]
