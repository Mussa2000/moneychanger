

from django.urls import include, path

urlpatterns = [
    path("approval_actions/", include('approval_engine.approval_actions.urls')),
    path("approval_group_actions/", include('approval_engine.approval_group_actions.urls')),
    path("approval_group_levels/", include('approval_engine.approval_group_levels.urls')),
    path("approval_group_marks/", include('approval_engine.approval_group_marks.urls')),
    path("approval_groups/", include('approval_engine.approval_groups.urls')),
    path("approval_levels/", include('approval_engine.approval_levels.urls')),
    path("approval_marks/", include('approval_engine.approval_marks.urls')),
    path("approval_tickets/", include('approval_engine.approval_tickets.urls')),
    path("approvers/", include('approval_engine.approvers.urls')),
]
