from django import forms
from .models import ApprovalGroupLevel, ApprovalGroupLevelProxy
from helpers import SubmitButtonHelper

class ApprovalGroupLevelForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalGroupLevel
        fields = "__all__"
        widgets = {
            'approval_group' : forms.HiddenInput(),
            'approval_ticket' : forms.HiddenInput()
        }

class ApprovalGroupLevelProxyForm(SubmitButtonHelper,forms.ModelForm):
    class Meta:
        model = ApprovalGroupLevelProxy
        fields = "__all__"
        widgets = {
            'approval_group' : forms.HiddenInput(),
            'approval_ticket' : forms.HiddenInput()
        }
        