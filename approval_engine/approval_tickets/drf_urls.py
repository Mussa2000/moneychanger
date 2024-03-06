from django.urls import path
from .drf_views import (
    ApprovalTicketDeleteAPIView,
    ApprovalTicketListAPIView,
    ApprovalTicketCreateAPIView,
    ApprovalTicketUpdateAPIView,
    ApprovalTicketDetailAPIView
)


urlpatterns = [
    path("list/", ApprovalTicketListAPIView.as_view(), name="list-approval_tickets"),
    path("detail/<int:pk>/", ApprovalTicketDetailAPIView.as_view(), name="detail-approval_ticket"),
    path("create/", ApprovalTicketCreateAPIView.as_view(), name="create-approval_ticket"),
    path("update/<int:pk>/", ApprovalTicketUpdateAPIView.as_view(), name="update-approval_ticket"),
    path("delete/<int:pk>/", ApprovalTicketDeleteAPIView.as_view(), name="delete-approval_ticket"),
]
