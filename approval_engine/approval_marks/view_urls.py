from django.urls import path
from .views import (
    ApprovalMarkCreateView,
    ApprovalMarkDeleteView,
    ApprovalMarkDetailView,
    ApprovalMarkListView,
    ApprovalMarkUpdateView
)

urlpatterns = [
    path('list/', ApprovalMarkListView.as_view(), name="list-approval_marks-view"),
    path('create/', ApprovalMarkCreateView.as_view(), name='create-approval_mark-view'),
    path('delete/<int:pk>/', ApprovalMarkDeleteView.as_view(), name="delete-approval_mark-view"),
    path('detail/<int:pk>/', ApprovalMarkDetailView.as_view(), name="detail-approval_mark-view"),  
    path('update/<int:pk>/', ApprovalMarkUpdateView.as_view(), name="update-approval_mark-view"),
]
