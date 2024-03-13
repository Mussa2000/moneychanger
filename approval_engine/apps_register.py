
from django.urls import include, path


apps_to_register = [
    "approval_actions",
    "approval_group_actions",
    "approval_group_levels",
    "approval_group_marks",
    "approval_groups",
    "approval_levels",
    "approval_marks",
    "approval_tickets",
    "approvers"
]

apps_to_register = list(map(lambda app : f"approval_engine.{app}", apps_to_register))

# urls_to_register = list(map(lambda app: path(f'{app}/', include(f"{app}.urls")), apps_to_register))

# print(urls_to_register)