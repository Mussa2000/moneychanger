from django import forms
from .models import ApprovalGroup, ApprovalGroupProxy
from helpers import SubmitButtonHelper

class ApprovalGroupForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalGroup
        fields = "__all__"
        
        widgets = {'approval_ticket' : forms.HiddenInput()}
        help_texts = {
            'name' : 'Name your group, for example Reviewer Group or Finance Group'
        }

class ApprovalGroupProxyForm(SubmitButtonHelper, forms.ModelForm):
    class Meta:
        model = ApprovalGroupProxy
        fields = '__all__'
        widgets = {
            'approval_ticket': forms.HiddenInput()
        }