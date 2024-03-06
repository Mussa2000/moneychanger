from django.contrib import admin
from approval_engine.approval_group_levels.models import ApprovalGroupLevel, ApprovalGroupLevelProxy

# Register your models here.
admin.site.register(ApprovalGroupLevel)
admin.site.register(ApprovalGroupLevelProxy)
