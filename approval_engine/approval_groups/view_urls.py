from django.urls import path
from .views import (
    ApprovalGroupCreateView,
    ApprovalGroupDeleteView,
    ApprovalGroupDetailView,
    ApprovalGroupListView,
    ApprovalGroupProxyDetailView,
    ApprovalGroupUpdateView,
    ApprovalGroupProxyCreateView,
    ApprovalGroupProxyDeleteView
)

urlpatterns = [
    path('proxy/delete/<int:pk>/', ApprovalGroupProxyDeleteView.as_view(), name="delete-approval_group_proxy-view"),
    path("proxy/create/", ApprovalGroupProxyCreateView.as_view(), name="create-approval_group_proxy-view"),
    path("proxy/detail/<int:pk>/", ApprovalGroupProxyDetailView.as_view(), name="detail-approval_group_proxy-view"),
    path('list/', ApprovalGroupListView.as_view(), name="list-approval_groups-view"),
    path('create/', ApprovalGroupCreateView.as_view(), name='create-approval_group-view'),
    path('delete/<int:pk>/', ApprovalGroupDeleteView.as_view(), name="delete-approval_group-view"),
    path('detail/<int:pk>/', ApprovalGroupDetailView.as_view(), name="detail-approval_group-view"),  
    path('update/<int:pk>/', ApprovalGroupUpdateView.as_view(), name="update-approval_group-view"),
]
