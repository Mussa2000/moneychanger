from django.contrib import admin
from approval_engine.approvers.models import Approver, ApproverProxy

# Register your models here.
admin.site.register(Approver)
admin.site.register(ApproverProxy)
