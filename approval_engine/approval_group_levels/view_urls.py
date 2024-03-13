from django.urls import path
from .views import (
    ApprovalGroupLevelCreateView,
    ApprovalGroupLevelDeleteView,
    ApprovalGroupLevelDetailView,
    ApprovalGroupLevelListView,
    ApprovalGroupLevelProxyCreateView,
    ApprovalGroupLevelUpdateView,
    shift_approval_group_level_proxy_to_left,
    shift_approval_group_level_proxy_to_right,
    shift_approval_group_level_to_left,
    shift_approval_group_level_to_right,
    
)

urlpatterns = [
    path('list/', ApprovalGroupLevelListView.as_view(), name="list-approval_group_levels-view"),
    path('create/', ApprovalGroupLevelCreateView.as_view(), name='create-approval_group_level-view'),
    path('delete/<int:pk>/', ApprovalGroupLevelDeleteView.as_view(), name="delete-approval_group_level-view"),
    path('detail/<int:pk>/', ApprovalGroupLevelDetailView.as_view(), name="detail-approval_group_level-view"),  
    path('update/<int:pk>/', ApprovalGroupLevelUpdateView.as_view(), name="update-approval_group_level-view"),
    path('shift_right/<int:approval_group_level_pk>/', shift_approval_group_level_to_right, name='shift-approval_group_level_to_right-view'),
    path('shift_left/<int:approval_group_level_pk>/', shift_approval_group_level_to_left, name='shift-approval_group_level_to_left-view'),
    
    # proxies
    path('proxy/shift_right/<int:approval_group_level_proxy_pk>/', shift_approval_group_level_proxy_to_right, name='shift-approval_group_level_proxy_to_right-view'),
    path('proxy/shift_left/<int:approval_group_level_proxy_pk>/', shift_approval_group_level_proxy_to_left, name='shift-approval_group_level_proxy_to_left-view'),
    path("proxy/create/", ApprovalGroupLevelProxyCreateView.as_view(), name="create-approval_group_level_proxy-view"),
]
