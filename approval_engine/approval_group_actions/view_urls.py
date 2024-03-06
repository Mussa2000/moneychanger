from django.urls import path
from .views import (
    ApprovalGroupActionCreateView,
    ApprovalGroupActionDeleteView,
    ApprovalGroupActionDetailView,
    ApprovalGroupActionListView,
    ApprovalGroupActionUpdateView
)

urlpatterns = [
    path('list/', ApprovalGroupActionListView.as_view(), name="list-approval_group_actions-view"),
    path('create/', ApprovalGroupActionCreateView.as_view(), name='create-approval_group_action-view'),
    path('delete/<int:pk>/', ApprovalGroupActionDeleteView.as_view(), name="delete-approval_group_action-view"),
    path('detail/<int:pk>/', ApprovalGroupActionDetailView.as_view(), name="detail-approval_group_action-view"),  
    path('update/<int:pk>/', ApprovalGroupActionUpdateView.as_view(), name="update-approval_group_action-view"),
]
