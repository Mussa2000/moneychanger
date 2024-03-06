from django import forms
from .models import ApprovalLevel, ApprovalLevelProxy
from helpers import SubmitButtonHelper

class ApprovalLevelForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalLevel
        fields = "__all__"
        widgets = {
            'approval_group' : forms.HiddenInput()
        }
        help_texts = {
            'index' : 'This represents the position of the specified approver in the flow.'
        }

class ApprovalLevelProxyForm(SubmitButtonHelper, forms.ModelForm):
    class Meta:
        model = ApprovalLevelProxy
        fields = '__all__'
        widgets = {
            'approval_group' : forms.HiddenInput()
        }
        