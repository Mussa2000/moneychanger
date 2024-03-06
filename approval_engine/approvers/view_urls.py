from django.urls import path
from .views import (
    ApproverCreateView,
    ApproverDeleteView,
    ApproverDetailView,
    ApproverListView,
    ApproverUpdateView
)

urlpatterns = [
    path('list/', ApproverListView.as_view(), name="list-approvers-view"),
    path('create/', ApproverCreateView.as_view(), name='create-approver-view'),
    path('delete/<int:pk>/', ApproverDeleteView.as_view(), name="delete-approver-view"),
    path('detail/<int:pk>/', ApproverDetailView.as_view(), name="detail-approver-view"),  
    path('update/<int:pk>/', ApproverUpdateView.as_view(), name="update-approver-view"),
]
