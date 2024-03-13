from django.urls import path
from .views import (
    ApprovalGroupMarkCreateView,
    ApprovalGroupMarkDeleteView,
    ApprovalGroupMarkDetailView,
    ApprovalGroupMarkListView,
    ApprovalGroupMarkUpdateView
)

urlpatterns = [
    path('list/', ApprovalGroupMarkListView.as_view(), name="list-approval_group_marks-view"),
    path('create/', ApprovalGroupMarkCreateView.as_view(), name='create-approval_group_mark-view'),
    path('delete/<int:pk>/', ApprovalGroupMarkDeleteView.as_view(), name="delete-approval_group_mark-view"),
    path('detail/<int:pk>/', ApprovalGroupMarkDetailView.as_view(), name="detail-approval_group_mark-view"),  
    path('update/<int:pk>/', ApprovalGroupMarkUpdateView.as_view(), name="update-approval_group_mark-view"),
]
