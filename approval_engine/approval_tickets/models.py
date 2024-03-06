import importlib
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from approval_engine.approval_actions.models import ApprovalAction
from approval_engine.approval_groups.models import ApprovalGroup, ApprovalGroupProxy

from approval_engine.shared.helpers.load_module import load_model_from_module 
# Create your models here.


class ApprovalTicket(models.Model, ):
    approval_actions_code = models.CharField(max_length=255, null=True)
    model_module_location = models.CharField(max_length=255)
    
    model_record_id = models.CharField(max_length=255)

    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="approval_tickets", blank=True, null=True)
    
    def __str__(self) -> str:
        return f"Approval Ticket: {self.get_action_model()}"
    def action_model_url(self):
        return self.get_action_model().get_absolute_url()

    def get_action_model(self):
        try:
            return load_model_from_module(
                self.model_module_location, self.model_record_id
            )
        except Exception as e:
            settings.LOGGER.error(e)
            return False
    
    def is_approved(self):
        approval_group_marks = self.approval_group_marks()
        # print([mark.action_status for mark in approval_group_marks])
        # input(len(approval_group_marks))
        # input(self.approval_group_levels.count())
        if len(approval_group_marks) == self.approval_group_levels.count():
            # This means all required marks have been submitted.
            # Check that all the group marks are 'accept'.
            if len(approval_group_marks) == 0:
                return False
            all_approval_group_marks_are_accepted = all(mark.action_status == 'accept' for mark in approval_group_marks)
            
            return all_approval_group_marks_are_accepted
        else:
            return False

        
    def is_denied(self):
        all_approval_group_marks_are_denied = all(map(lambda approval_group_mark : approval_group_mark.action_status == 'deny', self.approval_group_marks()))
        return all_approval_group_marks_are_denied
    
    def denied_group_mark(self):
        for approval_group_mark in self.approval_group_marks():
            if approval_group_mark.action_status == 'deny':
                return approval_group_mark
    
    def approval_group_marks(self):
        approval_group_marks = []
        
        for approval_group_level in self.approval_group_levels.all():
            if approval_group_level.approval_group_marks.first():
                approval_group_marks.append(approval_group_level.approval_group_marks.first())
        
        return approval_group_marks
            
            
    def ordered_approval_groups(self):
        # return ordered approval groups by level
        return ApprovalGroup.objects.filter(approval_ticket=self.pk).order_by('approval_group_levels__index')
    
    def execute_actions(self):
        actions_to_execute = ApprovalAction.objects.filter(code=self.approval_actions_code)
        for action in actions_to_execute:
                settings.LOGGER.debug(f"Executing action {action.module_to_execute_location}")
                imported_module = importlib.import_module(
                    action.module_to_execute_location
                )
                action = imported_module.Action()
                action.execute(self)


class ApprovalTicketProxy(models.Model, ):
    name = models.CharField(max_length=255, default="Approval Ticket Proxy")
    code = models.CharField(max_length=255, default="MEMBER_BLUEPRINT")
    approval_actions_code = models.CharField(max_length=255, null=True)
    model_module_location = models.CharField(max_length=255)
    
    model_record_id = models.CharField(max_length=255)

    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="approval_ticket_proxies", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def ordered_approval_groups(self):
        # return ordered approval groups by level
        return ApprovalGroupProxy.objects.filter(approval_ticket=self.pk).order_by('approval_levels__index')