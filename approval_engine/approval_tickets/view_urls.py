from django.urls import path
from .views import (
    ApprovalTicketCreateView,
    ApprovalTicketDeleteView,
    ApprovalTicketDetailView,
    ApprovalTicketListView,
    ApprovalTicketMarksDetailView,
    ApprovalTicketProxyCreateView,
    ApprovalTicketProxyDetailView,
    ApprovalTicketUpdateView,
    ApprovalTicketProxyListView,
    select_model_form_view,
    select_model_record_form_view,
    UserApprovalTicketDetailView,
)

urlpatterns = [
    path("proxy/list", ApprovalTicketProxyListView.as_view(), name="list-approval_ticket_proxies-view"),
    path("proxy/create/", ApprovalTicketProxyCreateView.as_view(), name="create-approval_ticket_proxy-view"),
    path("proxy/detail/<int:pk>", ApprovalTicketProxyDetailView.as_view(), name="detail-approval_ticket_proxy-view"),
    path("list/", ApprovalTicketListView.as_view(), name="list-approval_tickets-view"),
    path(
        "create/",
        ApprovalTicketCreateView.as_view(),
        name="create-approval_ticket-view",
    ),
    path(
        "delete/<int:pk>/",
        ApprovalTicketDeleteView.as_view(),
        name="delete-approval_ticket-view",
    ),
    path(
        "detail/<int:pk>/",
        ApprovalTicketDetailView.as_view(),
        name="detail-approval_ticket-view",
    ),
    path(
        "mark-details/<int:pk>/",
        ApprovalTicketMarksDetailView.as_view(),
        name="detail-approval_ticket_marks-view",
    ),
    # urls.py
    # massy
    path(
        "approval_tickets/user/<int:pk>/",
        UserApprovalTicketDetailView.as_view(),
        name="user-tickets-detail",
    ),
    # Add other URL patterns as needed
    path(
        "update/<int:pk>/",
        ApprovalTicketUpdateView.as_view(),
        name="update-approval_ticket-view",
    ),
    path("select/model/", select_model_form_view, name="select-model-view"),
    path(
        "select/<str:model_label>/",
        select_model_record_form_view,
        name="select-model_record-view",
    ),
]
