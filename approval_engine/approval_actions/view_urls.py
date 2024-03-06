from django.urls import path
from .views import (
    ApprovalActionCreateView,
    ApprovalActionDeleteView,
    ApprovalActionDetailView,
    ApprovalActionListView,
    ApprovalActionUpdateView
)

urlpatterns = [
    path('list/', ApprovalActionListView.as_view(), name="list-approval_actions-view"),
    path('create/', ApprovalActionCreateView.as_view(), name='create-approval_action-view'),
    path('delete/<int:pk>/', ApprovalActionDeleteView.as_view(), name="delete-approval_action-view"),
    path('detail/<int:pk>/', ApprovalActionDetailView.as_view(), name="detail-approval_action-view"),  
    path('update/<int:pk>/', ApprovalActionUpdateView.as_view(), name="update-approval_action-view"),
]
