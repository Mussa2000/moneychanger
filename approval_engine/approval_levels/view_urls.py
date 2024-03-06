from django.urls import path


from .views import (
    ApprovalLevelCreateView,
    ApprovalLevelDeleteView,
    ApprovalLevelDetailView,
    ApprovalLevelListView,
    ApprovalLevelProxyCreateView,
    ApprovalLevelUpdateView,
    ApprovalLevelProxyDeleteView,
    ApprovalLevelProxyUpdateView,
    shift_approval_level_to_down,
    shift_approval_level_to_up
)

urlpatterns = [
    path("proxy/delete/<int:pk>/", ApprovalLevelProxyDeleteView.as_view(), name="delete-approval_level_proxy-view"),
    path("proxy/create/", ApprovalLevelProxyCreateView.as_view(), name="create-approval_level_proxy-view"),
    path("proxy/updates/<int:pk>/", ApprovalLevelProxyUpdateView.as_view(), name="update-approval_level_proxy-view"),
    path('proxy/shift/down/<int:approval_level_pk>/', shift_approval_level_to_down, name="shift-approval_level_proxy_to_down-view"),
    path('proxy/shift/up/<int:approval_level_pk>/', shift_approval_level_to_up, name="shift-approval_level_proxy_to_up-view"),
    
    path('list/', ApprovalLevelListView.as_view(), name="list-approval_levels-view"),
    path('create/', ApprovalLevelCreateView.as_view(), name='create-approval_level-view'),
    path('delete/<int:pk>/', ApprovalLevelDeleteView.as_view(), name="delete-approval_level-view"),
    path('detail/<int:pk>/', ApprovalLevelDetailView.as_view(), name="detail-approval_level-view"),  
    path('update/<int:pk>/', ApprovalLevelUpdateView.as_view(), name="update-approval_level-view"),
    path('shift/down/<int:approval_level_pk>/', shift_approval_level_to_down, name="shift-approval_level_to_down-view"),
    path('shift/up/<int:approval_level_pk>/', shift_approval_level_to_up, name="shift-approval_level_to_up-view"),
]
