from django import forms
from .models import ApprovalMark
from helpers import SubmitButtonHelper

class ApprovalMarkForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalMark
        fields = "__all__"
        
        widgets = {
            'approval_level' : forms.HiddenInput()
        }
        
        help_texts = {
            'action_message' : 'This is required if you are performing a "DENY" action'
        }